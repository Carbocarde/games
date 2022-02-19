from abc import ABC, abstractmethod
from typing import List

import agent


class Game(ABC):
    @property
    @abstractmethod
    def min_players(self) -> int:
        """Property containing the min number of players"""
        pass

    @property
    @abstractmethod
    def max_players(self) -> int:
        """Property containing the max number of players"""
        pass

    @property
    @abstractmethod
    def rec_players(self) -> int:
        """Property containing the recommended number of players"""
        pass

    @property
    @abstractmethod
    def deterministic(self) -> bool:
        """Property that determines if games with the same agents can result in different outcomes on new runs"""
        pass

    @abstractmethod
    def simulate(self, players: List[agent]) -> List[int]:
        """Simulate the game and return the index(s) of the winner(s)"""
        pass

    @abstractmethod
    def __str__(self):
        """Name of the game"""
        pass
