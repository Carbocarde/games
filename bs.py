from abc import ABC, abstractmethod
from collections.abc import Mapping
from enum import Enum
from typing import Union, NamedTuple, List, Optional
import random


class Suit(Enum):
    SPADES = 1
    CLUBS = 2
    HEARTS = 3
    DIAMONDS = 4


class Rank(Enum):
    ACE = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


def advance_rank(rank: Rank) -> Rank:
    return Rank((rank.value + 1 - Rank.ACE.value) % len(Rank) + Rank.ACE.value)


class Card(NamedTuple):
    suit: Suit
    rank: Rank


def create_deck(shuffle=True):
    deck = []
    for suit in Suit:
        for rank in Rank:
            deck += [Card(suit=suit, rank=rank)]
    if shuffle:
        random.shuffle(deck)

    return deck


BSPlayerID = int


class BSPlay(NamedTuple):
    player: BSPlayerID
    # Can't name this count for some reason
    number: int
    rank: Rank
    cards_played: Optional[List[Card]]


class BSCall(NamedTuple):
    caller: BSPlayerID
    callee: BSPlayerID
    discovered_lie: bool


class BSPickup(NamedTuple):
    cards: List[Card]


class BSInit(NamedTuple):
    players: List[BSPlayerID]
    card_counts: List[int]


BSEvent = Union[BSInit, BSPlay, BSCall, BSPickup]


class BSAgent(ABC):
    @abstractmethod
    def request_play(self, rank: Rank) -> BSPlay:
        pass

    @abstractmethod
    def request_bs(self) -> bool:
        pass

    @abstractmethod
    def inform_event(self, event: BSEvent):
        pass


class StdioBSAgent(BSAgent):
    hand: List[Card]

    def __init__(self, ident: BSPlayerID):
        self.ident = ident
        self.hand = []

    def print(self, *args, **kwargs):
        print(str(self.ident) + ": ", end="")
        print(*args, **kwargs)

    def request_play(self, rank: Rank):
        self.print("Play requested of rank {}".format(rank))
        self.print("Provide space seperated list of cards you want to play")
        cards = [self.hand[int(i)] for i in input().split(" ")]
        return BSPlay(
            player=self.ident, number=len(cards), rank=rank, cards_played=cards
        )

    def request_bs(self) -> bool:
        self.print("Call bs? y/n")
        return input() == "y"

    def inform_event(self, event: BSEvent):
        if type(event) == BSPickup:
            for i, card in enumerate(event.cards):
                self.print(i, card)
            self.hand += event.cards
        else:
            self.print(event)


class BSGame:
    order: List[BSPlayerID]
    players: Mapping[BSPlayerID, BSAgent]
    hands: dict[BSPlayerID, set[Card]]

    def __init__(self, players: Mapping[BSPlayerID, BSAgent]):
        self.players = players
        self.order = list(self.players.keys())
        random.shuffle(self.order)
        self.deck = create_deck()
        self.hands = {}

    def deal(self):
        total_cards = len(self.deck)
        cards_per_player = total_cards // len(self.players)
        cards_remaining = total_cards % len(self.players)
        for i, pid in enumerate(self.order):
            self.hands[pid] = set(
                self.deck[i * cards_per_player : (i + 1) * cards_per_player]
            )
        for i, pid in enumerate(self.order):
            if i >= cards_remaining:
                break
            self.hands[pid] += [self.deck[-i]]
        self.deck = []

    def inform_hands(self):
        for pid in self.players.keys():
            self.players[pid].inform_event(BSPickup(cards=self.hands[pid]))

    def inform_init(self):
        counts = [len(self.hands[pid]) for pid in self.order]
        for pid in self.order:
            self.players[pid].inform_event(
                BSInit(players=self.order, card_counts=counts)
            )

    def play(self):
        self.deal()
        self.inform_init()
        self.inform_hands()

        current_rank = Rank.ACE
        while True:
            # Forget ace of spades starts. That isn't really a necessary rule
            for pid in self.order:
                play = self.players[pid].request_play(current_rank)
                assert play.rank == current_rank
                assert play.cards_played is not None
                assert len(play.cards_played) == play.number
                for card in play.cards_played:
                    assert card in self.hands[pid]

                self.hands[pid] -= set(play.cards_played)

                bs = False
                for card in play.cards_played:
                    if card.rank != current_rank:
                        bs = True
                        break

                self.deck += play.cards_played

                for inform_pid in self.order:
                    self.players[inform_pid].inform_event(
                        BSPlay(
                            player=pid,
                            number=play.number,
                            rank=current_rank,
                            cards_played=None,
                        )
                    )

                bs_callers = []
                for bs_pid in self.order:
                    if bs_pid == pid:
                        continue
                    if self.players[bs_pid].request_bs():
                        bs_callers += [bs_pid]

                if len(bs_callers) != 0:
                    bs_caller = random.choice(bs_callers)

                    if bs:
                        call = BSCall(caller=bs_caller, callee=pid, discovered_lie=bs)
                        for pid in self.order:
                            self.players[pid].inform_event(call)
                        self.players[pid].inform_event(BSPickup(self.deck))
                        self.deck = []

                if len(self.hands[pid]) == 0:
                    winner = pid
                    break
                current_rank = advance_rank(current_rank)


agents = {1: StdioBSAgent(1), 2: StdioBSAgent(2)}
game = BSGame(agents)
game.play()
