# main.py

from fair_die import FairDie
from human_player import HumanPlayer
from computer_player import ComputerPlayer
from game import Game


def main() -> None:
    print("Welcome to Dice Battle with HP!\n")
    player_name = input("Enter your name: ")

    human_die = FairDie()
    computer_die = FairDie()

    human = HumanPlayer(player_name, human_die)
    computer = ComputerPlayer("Computer", computer_die)

    battle = Game(human, computer)
    battle.play_game()


if __name__ == "__main__":
    main()
