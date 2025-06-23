# loaded_die.py

import random
from die import Die


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
        return random.choices(faces, weights=weights, k=1)[0]
