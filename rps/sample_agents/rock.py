from rps import Choice, RPSPlay, RPSAgent


class Player(RPSAgent):
    def choose(self) -> RPSPlay:
        return RPSPlay(Choice.ROCK)


if __name__ == "__main__":
    Player(1).play()
