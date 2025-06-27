# human_player.py

from player import Player

class HumanPlayer(Player):
    """
    A human-controlled player who rolls on user prompt.
    """

    def roll_dice(self) -> int:
        """
        Prompt the user, roll the die, print and return the result.
        """
        input(f"{self.name}, press Enter to roll the die...")
        result = self.die.roll()
        print(f"{self.name} rolled: {result}")
        return result
