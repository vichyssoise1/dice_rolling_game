# player.py

from abc import ABC, abstractmethod
from health_bar import HealthBar


class Player(ABC):
    """
    Abstract base class for a player in Dice Battle,
    now with health points.
    """

    def __init__(self, name: str, die, maximum_health: int = 30) -> None:
        self.name = name
        self.die = die
        self.health_bar = HealthBar(maximum_health)

    @abstractmethod
    def roll_dice(self) -> int:
        pass

    def take_damage(self, amount: int) -> None:
        self.health_bar.take_damage(amount)

    def is_alive(self) -> bool:
        return self.health_bar.is_alive()
