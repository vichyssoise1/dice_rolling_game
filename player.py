# player.py

from abc import ABC, abstractmethod

class Player(ABC):

    def __init__(self, name: str, die) -> None:
        """
        Initialize the player with a name and a Die instance.

        :param name: The player's name.
        :param die:   A Die-like object (must implement roll()).
        """
        self.name = name
        self.die = die

    def roll_dice(self) -> int:
        pass
