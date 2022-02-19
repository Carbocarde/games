"""
The base class for a generic game
"""
from abc import ABC, abstractmethod
from typing import List

from agent import Agent


class Game(ABC):
    """
    A game capable of having it's players ranked
    """

    @property
    @abstractmethod
    def min_players(self) -> int:
        """Property containing the min number of players"""

    @property
    @abstractmethod
    def max_players(self) -> int:
        """Property containing the max number of players"""

    @property
    @abstractmethod
    def rec_players(self) -> int:
        """Property containing the recommended number of players"""

    @property
    @abstractmethod
    def deterministic(self) -> bool:
        """
        Property that determines if games with the same agents can result in different outcomes  on
        new runs
        """

    @abstractmethod
    def simulate(self, players: List[Agent]) -> List[int]:
        """Simulate the game and return the index(s) of the winner(s)"""

    @abstractmethod
    def __str__(self):
        """Name of the game"""
