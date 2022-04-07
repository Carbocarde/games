"""Transmittable actions that agents can do"""
from enum import Enum
from typing import Optional

from action import Action


class Choice(Enum):
    """Possible plays"""

    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class RPSPlay(Action):
    """Object representing a player declaring its choice"""

    def __init__(self, choice: Optional[Choice] = None):
        self.choice = choice

    def __str__(self):
        if self.choice is None:
            raise ValueError("No choice declared!")
        return str(self.choice.value)

    def parse(self, msg):
        """Parse the choice"""
        self.choice = Choice(int(msg))
        return self.choice
