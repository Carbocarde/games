from typing import List

from game import Game
from rps import rps_actions, RPSPlay


class RPSGame(Game):
    """A game of rock paper scissors"""

    min_players = 2
    max_players = 2
    rec_players = 2
    deterministic = False
    player_ports = [5000, 5002]

    def simulate(self, players: List[str]) -> List[int]:
        if len(players) != 2:
            raise ValueError("Invalid number of players")

        sockets = self.open_sockets()
        player_procs = self.boot_players(players)
        sockets = self.connect(sockets)

        parser = RPSPlay()
        choices = []
        for socket in sockets:
            msg = socket.recv(1024).decode()
            choice = parser.parse(msg)
            choices.append(choice)

        self.kill_players(player_procs)

        if choices[0] == choices[1]:
            return []
        elif (choices[0].value + 1) % 3 == choices[1].value:
            return [1]
        else:
            return [0]

    def __str__(self):
        return "Rock Paper Scissors"


if __name__ == "__main__":
    players = ["sample_agents/paper.py", "sample_agents/scissors.py"]
    game = RPSGame()
    winner = game.simulate(players=players)
    print(winner)
