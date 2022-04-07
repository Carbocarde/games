from abc import ABC, abstractmethod

from rps import RPSPlay

from agent import Agent


class RPSAgent(Agent, ABC):
    def __init__(self, id: int, port: int):
        self.id = str(id)
        super().__init__(port)

    def play(self):
        choice = self.choose()
        self.post_message(choice)

    @abstractmethod
    def choose(self) -> RPSPlay:
        """Choose your move"""

    def __str__(self):
        return self.id

    def __hash__(self):
        return self.id.__hash__()
