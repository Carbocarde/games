"""
Ranking methods for agents in a game.
TODO: Add ELO ratings
"""
import itertools
import random
from typing import List, Dict, Optional

from agent import Agent
from game import Game


def random_combinations(arr: list, size: int, count: int) -> list:
    """
    Return a random subset of combinations
    :param arr: source array
    :param size: size of a combination
    :param count: number of combinations to return
    """
    combinations = list(itertools.combinations(arr, size))
    output = []
    while count > len(combinations):
        output += combinations
        count -= len(combinations)

    indices = random.sample(range(len(combinations)), count)
    return output + [combinations[i] for i in indices]


class Rank:
    """
    Represents the ranking process
    """

    def __init__(self, game: Game, agents: List[Agent]):
        self.agents = agents
        self.game = game
        self.ranking: Optional[Dict[Agent, int]] = None

    def rank(self, runs: int = 1000):
        """
        Give the agents in the game a score
        :return: agent -> score mapping
        """
        player_count = self.game.rec_players
        if player_count > len(self.agents):
            player_count = self.game.min_players

        if player_count > len(self.agents):
            raise ValueError("Not enough agents to simulate a game!")

        wins = dict.fromkeys(self.agents, 0)

        if self.game.deterministic:
            # Do an exhaustive search
            combinations = itertools.combinations(self.agents, player_count)
        else:
            # Run a lot of random games and it'll average itself out
            combinations = random_combinations(self.agents, player_count, runs)

        for combination in combinations:
            winners = self.game.simulate(combination)
            for winner in winners:
                wins[combination[winner]] += 1

        self.ranking = wins

    def __str__(self):
        ranking = "Agents not ranked! Run .rank() to generate rankings."

        if self.ranking is not None:
            ranking = ""
            for agent, score in self.ranking.items():
                ranking += str(score) + " " + str(agent) + "\n"

        return (
            "Game"
            + str(self.game)
            + "Agents:"
            + str(self.agents)
            + "Ranking: "
            + ranking
        )
