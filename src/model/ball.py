"""Defining the ball class."""

from constants import BALL_RADIUS, MAX_X, MAX_Y
from model.vector import Vector

class Ball:
    radius: int = BALL_RADIUS
    vector: Vector
    x: int
    y: int
    
    def __init__(self, vector, x: int, y: int) -> None:
        """Constructor for the ball object."""
        
        # TODO: Parameter validation.
        self.vector = vector
        self.x = x
        self.y = y
        
    def change_directions(self, vector):
        """Changes the direction vector."""
        self.vector = vector
        
    def set_x(self, x):
        """Setter for the x position."""        
        self.x = x
        
    def set_y(self, y):
        """setter for the y position."""       
        self.y = y
        
    def tick(self):
        """Updates the position of the ball based on the current position and direction vector."""
        self.set_x(self.x + self.vector.x_vector)
        self.set_y(self.y + self.vector.y_vector)