"""Define action serializer/parser"""
from abc import ABC, abstractmethod


class Action(ABC):
    """Represents an action the player or game can make"""

    def send(self):
        """Send the action"""
        print(str(self))

    @abstractmethod
    def parse(self, msg: str):
        """Parse the action from the str representation into the class representation"""

    @abstractmethod
    def __str__(self):
        """Represent the action in a way that can be transmitted"""
