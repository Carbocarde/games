from abc import ABC, abstractmethod

from rps import RPSPlay

from agent import Agent


class RPSAgent(Agent, ABC):
    def __init__(self, id: int):
        self.id = str(id)

    def play(self):
        choice = self.choose()
        choice.send()

    @abstractmethod
    def choose(self) -> RPSPlay:
        """Choose your move"""

    def __str__(self):
        return self.id

    def __hash__(self):
        return self.id.__hash__()
