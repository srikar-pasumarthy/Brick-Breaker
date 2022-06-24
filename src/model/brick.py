"""Defining the class for a brick."""


class Brick:
    color: str
    health: int
    x: int
    y: int
    type: str
    
    def __init__(self, type, x, y) -> None:
        """Constructor for the brick class."""
        if type == "one":
            self.color = "#EBFE05"
            self.health = 1
        elif type == "two":
            self.color = "#05DCFE"
            self.health = 2
        elif type == "three":
            self.color = "#9405FE"
            self.health = 3
        else:
            raise ValueError("Invalid brick type. Valid types are one, two, and three")
        
        # These values will represent the upper left corner of the brick.
        self.x = x
        self.y = y
        self.type = type
        
    def is_dead(self) -> bool:
        """Checks to see if the brick has any health."""
        return True if self.health == 0 else False
    
    def hit_brick(self) -> None:
        """Reduces the health of the brick."""
        self.health -= 1