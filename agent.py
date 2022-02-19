"""
The base class for a generic agent
"""
from abc import abstractmethod


class Agent:
    """a rank-able agent"""

    @abstractmethod
    def __str__(self):
        """Name of the agent"""

    @abstractmethod
    def __hash__(self):
        """Needed to use this as a key for a dict"""
