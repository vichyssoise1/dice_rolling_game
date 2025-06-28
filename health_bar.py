# health_bar.py

class HealthBar:
    """
    Encapsulates a character's health.
    """

    def __init__(self, maximum_health: int) -> None:
        self.maximum_health = maximum_health
        self.current_health = maximum_health

    def take_damage(self, amount: int) -> None:
        """Reduce current health, floored at zero."""
        self.current_health = max(self.current_health - amount, 0)

    def is_alive(self) -> bool:
        """Check if health is still above zero."""
        return self.current_health > 0

    def __str__(self) -> str:
        """
        Return a simple text bar, e.g. [#####-----] 5/10
        """
        total_slots = 10
        filled_slots = int((self.current_health / self.maximum_health) * total_slots)
        bar = "[" + "#" * filled_slots + "-" * (total_slots - filled_slots) + "]"
        return f"{bar} {self.current_health}/{self.maximum_health}"
