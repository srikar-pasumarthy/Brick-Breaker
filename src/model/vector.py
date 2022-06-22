"""Defining a basic vector class that will be used to describe the ball's movement."""

class Vector:
    x_vector: int
    y_vector: int
    
    def __init__(self, x_vector, y_vector) -> None:
        """Constructor for the vector Class."""
        self.x_vector = x_vector
        self.y_vector = y_vector
        
    def set_x_vector(self, x_vector) -> None:
        """Changes the x vector."""
        self.x_vector = x_vector
                
    def set_y_vector(self, y_vector) -> None:
        """Changes the y vector."""
        self.y_vector = y_vector