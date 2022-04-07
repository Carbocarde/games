"""
The base class for a generic agent
"""
from abc import abstractmethod, ABC
import socket

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


class SocketAgent:
    """a agent capable of sending/receiving messages"""

    def __init__(self, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(("127.0.0.1", port))

    def parse_message(self, action: Action) -> Action:
        """Parse a message"""
        msg = self.s.recv(1024).decode()
        action.parse(msg)
        return action

    def post_message(self, action: Action):
        """Send a message to the game"""
        self.s.send(str(action).encode())


class Agent(RankableAgent, SocketAgent, ABC):
    """Game agent"""
