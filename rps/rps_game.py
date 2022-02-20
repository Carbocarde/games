from typing import List

from game import Game


class RPSGame(Game):
    """A game of rock paper scissors"""

    min_players = 2
    max_players = 2
    rec_players = 2
    deterministic = False

    def simulate(self, players: list) -> List[int]:
        """TODO: This. Players should be separate processes?"""
        if len(players) != 2:
            raise ValueError("Invalid number of players")

        return [0]

    def __str__(self):
        return "Rock Paper Scissors"
