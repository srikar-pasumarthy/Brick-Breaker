"""Main file for the program."""

from constants import START_VELOCITY_X, START_VELOCITY_Y, START_X, START_Y
from model.ball import Ball
from model.board import Board
from model.brick import Brick
from model.model import Model
from model.vector import Vector
from view.screen import ViewController


def main() -> None:
    """Launches the brick breaker game."""
    ball = Ball(Vector(START_VELOCITY_X, START_VELOCITY_Y), START_X, START_Y)
    board = Board()
    brick1 = Brick("one", -150, 0)
    brick2 = Brick("one", 100, 0)
    brick3 = Brick("two", 100, 20)
    brick4 = Brick("three", 100, 40)
    bricks = [brick1, brick2, brick3, brick4]
    model = Model(ball, board, bricks)
    view_controller = ViewController(model)
    view_controller.start_simulation()
    
if __name__ == "__main__":
    main()