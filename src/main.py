"""Main file for the program."""

from constants import LEVEL_ONE_BRICKS, START_VELOCITY_X, START_VELOCITY_Y, START_X, START_Y
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
    model = Model(ball, board, LEVEL_ONE_BRICKS)
    view_controller = ViewController(model)
    view_controller.start_simulation()
    
if __name__ == "__main__":
    main()