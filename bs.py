from abc import ABC, abstractmethod
from typing import List

from card import Card

class BaseAgent(ABC):
    def __init__(self, cards: List[Card]):
        self.cards = cards

    @abstractmethod
    def place_cards(self) -> List[Card]:
        """
        Choose cards to place down
        """
        pass

    @abstractmethod
    def call_bs(self, player: int, rank: str, count: int) -> bool:
        """
        Choose to call bs on the most recent card placement
        player: player that placed cards down
        rank: type of card played
        count: number of cards placed down by player
        """
        pass


class Game:
    def __init__(self):
        self.agents = []

    def add_agent(self, agent: BaseAgent):
        self.agents.append(agent)

    def simulate(self) -> int:
        """
        Simulate the game and return the ID of the victor
        """
        pass