# die.py

import random


class Die:
    """
    A generic die with a given number of sides.
    """

    def __init__(self, number_of_sides: int = 6) -> None:
        """
        Initialize the die with the specified number of sides.

        :param number_of_sides: Number of faces on the die (default: 6).
        """
        self.number_of_sides = number_of_sides

    def roll(self) -> int:
        """
        Roll the die and return a random face value between 1 and number_of_sides.

        :return: An integer result of the die roll.
        """
        return random.randint(1, self.number_of_sides)
