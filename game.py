# game.py

from typing import Optional
from player import Player


class Game:
    def __init__(self, player_one: Player, player_two: Player, rounds_to_win: int = 3) -> None:
        self.player_one = player_one
        self.player_two = player_two
        self.rounds_to_win = rounds_to_win
        self.score_one = 0
        self.score_two = 0

    def play_round(self) -> Optional[Player]:
        roll_one = self.player_one.roll_dice()
        roll_two = self.player_two.roll_dice()

        if roll_one > roll_two:
            self.score_one += 1
            print(f"{self.player_one.name} wins the round!\n")
            return self.player_one
        elif roll_two > roll_one:
            self.score_two += 1
            print(f"{self.player_two.name} wins the round!\n")
            return self.player_two
        else:
            print("It's a tie! No score change.\n")
            return None

    def display_score(self) -> None:
        print(f"Score → {self.player_one.name}: {self.score_one} | {self.player_two.name}: {self.score_two}\n")

    def play_game(self) -> Player:
        print(f"First to {self.rounds_to_win} wins!\n")
        while self.score_one < self.rounds_to_win and self.score_two < self.rounds_to_win:
            self.play_round()
            self.display_score()

        winner = self.player_one if self.score_one >= self.rounds_to_win else self.player_two
        print(f"🏆 {winner.name} is the champion! 🏆")
        return winner
