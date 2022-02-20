"""
The base class for a generic agent
"""
from abc import abstractmethod, ABC

from action import Action


class RankableAgent:
    """a rank-able agent"""

    @abstractmethod
    def play(self):
        """Play the game (wait for input or send a message)"""

    @abstractmethod
    def __str__(self):
        """Name of the agent"""

    @abstractmethod
    def __hash__(self):
        """Needed to use this as a key for a dict"""


class StdioAgent:
    """a agent capable of sending/receiving messages"""

    def parse_message(self, action: Action) -> Action:
        """Parse a message"""
        msg = input()
        action.parse(msg)
        return action

    def post_message(self, action: Action):
        """Send a message to the game"""
        action.send()


class Agent(RankableAgent, StdioAgent, ABC):
    """Game agent"""
