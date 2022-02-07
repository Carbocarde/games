from abc import ABC, abstractmethod
from typing import List


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class BaseAgent(ABC):
    @abstractmethod
    def place_cards(self) -> List[Card]:
        """
        Choose cards to place down
        """
        pass

    def call_bs(self) -> bool:
        """
        Choose to call bs on the most recent card placement
        """
        pass


class Game:
    def __init__(self):
        self.agents = []

    def addAgent(self, agent: BaseAgent):
        self.agents.append(agent)

    def simulate(self) -> int:
        """
        Simulate the game and return the ID of the victor
        """
        pass