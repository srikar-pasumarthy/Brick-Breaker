"""Represents a board object that the user controls."""

from tkinter.tix import MAX
from constants import BOARD_LENGTH, BOARD_START_X, BOARD_START_Y, MAX_X

MOVE_LENGTH: int = 25

class Board:
    """Board of a user.
        Can move right or left with user input."""
    x: int = BOARD_START_X
    y: int = BOARD_START_Y
    length: int = BOARD_LENGTH
    
    def move_left(self) -> None:
        """Moves the board to the left if possible."""
        if self.x - MOVE_LENGTH > -MAX_X:
            self.x -= MOVE_LENGTH
        elif self.x - MOVE_LENGTH <= -MAX_X:
            self.x = -MAX_X + 0.5 * self.length
        
    def move_right(self) -> None:
        """Moves the board to the right if possible."""
        if self.x + MOVE_LENGTH < MAX_X:
            self.x += MOVE_LENGTH
        elif self.x + MOVE_LENGTH >= MAX_X:
            self.x = MAX_X - 0.5 * self.length