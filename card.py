from enum import Enum
from random import shuffle
from typing import List

class Suit(Enum):
    CLUB    = 1
    HEART   = 2
    DIAMOND = 3
    SPADE   = 4

class Rank(Enum):
    ACE     = 1
    TWO     = 2
    THREE   = 3
    FOUR    = 4
    FIVE    = 5
    SIX     = 6
    SEVEN   = 7
    EIGHT   = 8
    NINE    = 9
    TEN     = 10
    JACK    = 11
    QUEEN   = 12
    KING    = 13
    
class Card:
    # maybe we need to worry about accidental mutation of cards... curse python for not
    # having constants

    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return f"{self.rank.name.lower()} of {self.suit.name.lower()}s"
    
    def __eq__(self, other) -> bool:
        return self.suit == other.suit and \
               self.rank == other.rank

class Deck:
    def __init__(self, number_of_decks: int):
        assert(number_of_decks > 0)
        self.number_of_decks = number_of_decks

        self.reset()
    
    def reset(self):
        """
        Reset the deck by creating this.number_of_decks cards. Worth noting that this
        creates entirely new objects, so any existing references are lost. This shouldn't
        be an issue, but if it ever becomes one, this may need a rework
        """

        self.cards = []
        for i in range(self.number_of_decks):
            for suit in Suit:
                for rank in Rank:
                    self.cards.append(Card(suit, rank))

        self.number_of_cards_dealt = 0
    
    def shuffle(self):
        """
        Shuffles the deck. All cards go back into the deck (in other words, all cards
        in the deck will be considered "not dealt")
        """

        shuffle(self.cards)
        self.number_of_cards_dealt = 0
    
    def get_number_of_cards_left_in_deck(self) -> int:
        """
        Gets the number of cards left in the deck.
        """

        return len(self.cards) - self.number_of_cards_dealt

    def deal(self, number_of_cards: int) -> List[Card]:
        """
        Deals the specified number of cards and returns them with a list. Returns an empty
        list if all cards have been dealt. If more cards are requested than are available,
        then all the remaining cards will be dealt
        """
        assert(number_of_cards > 0)
        
        cards_left_in_deck = self.get_number_of_cards_left_in_deck()
        number_of_cards = min(number_of_cards, cards_left_in_deck)
        
        dealt_cards = self.cards[self.number_of_cards_dealt:(self.number_of_cards_dealt + number_of_cards)]

        self.number_of_cards_dealt += number_of_cards

        return dealt_cards
