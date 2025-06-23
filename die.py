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


class FairDie(Die):
    """
    A fair die that behaves exactly like a standard die.
    """
    pass


class LoadedDie(Die):
    """
    A loaded die that favors higher face values.
    """

    def roll(self) -> int:
        """
        Roll the loaded die with bias towards higher numbers.
        Each face value i has weight i, so higher faces are more likely.
        """
        faces = list(range(1, self.number_of_sides + 1))
        weights = faces  # weight proportional to face value
        # random.choices returns a list, so grab the first element
        return random.choices(faces, weights=weights, k=1)[0]
