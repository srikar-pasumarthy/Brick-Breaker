"""Defining some constants that will be universally used in all files."""

from model.brick import Brick

# Constants relating to the size of the screen.
MAX_X: int = 250
MAX_Y: int = 250

# Constants relating to ball.
BALL_RADIUS: int = 10
START_X: int = 0
START_Y: int = 10
START_VELOCITY_X: int = 5
START_VELOCITY_Y: int = -5

# Constants relating to the board.
BOARD_START_X: int = 0
BOARD_START_Y: int = -220
BOARD_LENGTH: int = 75

# Constants relating to the brick.
BRICK_HEIGHT: int = 20
BRICK_LENGTH: int = 75

# Constants relating to level 1.
brick1 = Brick("one", -225, 100)
brick2 = Brick("one", -150, 100)
brick3 = Brick("one", -75, 100)
brick4 = Brick("one", 0, 100)
brick5 = Brick("one", 75, 100)
brick6 = Brick("one", 150, 100)

brick8 = Brick("two", -150, 120)
brick9 = Brick("two", -75, 120)
brick10 = Brick("two", 0, 120)
brick11 = Brick("two", 75, 120)

brick13 = Brick("three", -75, 140)
brick14 = Brick("three", 0, 140)
    
LEVEL_ONE_BRICKS = [brick1, brick2, brick3, brick4, brick5, brick6, 
                    brick8, brick9, brick10, brick11, brick13, brick14]