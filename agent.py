from abc import abstractmethod


class Agent:
    @abstractmethod
    def __str__(self):
        """Name of the agent"""
        pass

    @abstractmethod
    def __hash__(self):
        """Needed to use this as a key for a dict"""
        pass
