"""
Ranking methods for agents in RPS.
"""
from typing import List

from rank import Rank
from rps import RPSGame


class RPSRank(Rank):
    """Rank RPS agents"""

    def __init__(self, agents: List[str]):
        super().__init__(RPSGame(), agents)


if __name__ == "__main__":
    agent_paths = [
        "sample_agents/rock.py",
        "sample_agents/paper.py",
        "sample_agents/scissors.py",
    ]
    ranker = RPSRank(agent_paths)
    ranker.rank(100)
    print(str(ranker))
