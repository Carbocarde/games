import argparse

from rps import Choice, RPSPlay, RPSAgent


class Player(RPSAgent):
    def choose(self) -> RPSPlay:
        return RPSPlay(Choice.SCISSORS)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="id", help="Bot Id Str")
    parser.add_argument(
        dest="port", type=int, help="Server port that the bot should connect to."
    )

    args = parser.parse_args()
    Player(args.id, args.port).play()
