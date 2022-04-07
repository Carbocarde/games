"""
The base class for a generic game
"""
import subprocess
from abc import ABC, abstractmethod
import socket
from typing import List

from agent import Agent


class Game(ABC):
    """
    A game capable of having it's players ranked
    """

    @property
    @abstractmethod
    def min_players(self) -> int:
        """Property containing the min number of players"""

    @property
    @abstractmethod
    def max_players(self) -> int:
        """Property containing the max number of players"""

    @property
    @abstractmethod
    def rec_players(self) -> int:
        """Property containing the recommended number of players"""

    @property
    @abstractmethod
    def deterministic(self) -> bool:
        """
        Property that determines if games with the same agents can result in different outcomes  on
        new runs
        """

    @property
    @abstractmethod
    def player_ports(self) -> List[int]:
        """Ports the players are connected on"""

    def open_sockets(self) -> List[socket.socket]:
        """Open ports for connection"""
        sockets = []
        for port in self.player_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(("", port))
            sockets.append(s)

        return sockets

    def connect(self, sockets: List[socket.socket]) -> List[socket.socket]:
        """Connect and return a list"""
        clients = []
        for s in sockets:
            s.listen(1)
            c, _ = s.accept()
            clients.append(c)

        return clients

    def boot_players(self, players: List[str]) -> List[subprocess.Popen]:
        """Boot a list of players and give them an Id and Socket to connect to."""
        player_procs = []
        for i, (player, port) in enumerate(zip(players, self.player_ports)):
            proc = subprocess.Popen(["python", player, str(i), str(port)])
            player_procs.append(proc)

        return player_procs

    def kill_players(self, players: List[subprocess.Popen]):
        for player in players:
            player.kill()

    @abstractmethod
    def simulate(self, players: List[str]) -> List[int]:
        """Simulate the game and return the index(s) of the winner(s) port(s)"""

    @abstractmethod
    def __str__(self):
        """Name of the game"""
