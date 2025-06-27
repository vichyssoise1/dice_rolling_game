# computer_player.py

from player import Player

class ComputerPlayer(Player):
    """
    An AI-controlled player who rolls automatically.
    """

    def roll_dice(self) -> int:
        """
        Automatically roll the die, print and return the result.
        """
        result = self.die.roll()
        print(f"{self.name} (Computer) rolled: {result}")
        return result
