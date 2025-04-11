"""File to define Bear class."""

__author__: str = "730826007"


class Bear:
    """Define Bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """One day."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Eat."""
        self.hunger_score += num_fish
