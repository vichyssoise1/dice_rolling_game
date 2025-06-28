# game.py

from player import Player


class Game:
    """
    Turn-based HP battle: each roll inflicts damage
    until one player's health reaches zero.
    """

    def __init__(self, player_one: Player, player_two: Player) -> None:
        self.attacker = player_one
        self.defender = player_two

    def play_turn(self) -> None:
        damage = self.attacker.roll_dice()
        self.defender.take_damage(damage)
        print(f"{self.attacker.name} deals {damage} damage!")
        print(f"{self.defender.name} HP: {self.defender.health_bar}\n")

    def play_game(self) -> Player:
        print("Battle start!\n")
        # Show initial health
        print(f"{self.attacker.name} HP: {self.attacker.health_bar}")
        print(f"{self.defender.name} HP: {self.defender.health_bar}\n")

        # Alternate turns until one falls
        while self.attacker.is_alive() and self.defender.is_alive():
            self.play_turn()
            # swap roles
            self.attacker, self.defender = self.defender, self.attacker

        winner = self.attacker if self.attacker.is_alive() else self.defender
        print(f"🏆 {winner.name} wins the battle! 🏆")
        return winner
