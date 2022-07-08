"""Represents the model of the simulation."""

from constants import BALL_RADIUS, BOARD_LENGTH, BRICK_HEIGHT, BRICK_LENGTH, MAX_X, MAX_Y
from model.ball import Ball
from model.board import Board
from model.brick import Brick
from model.vector import Vector

LAMDA: int = 3

class Model:
    """Model class."""
    time: int = 0
    ball: Ball
    board: Board
    bricks: list[Brick]
    
    def __init__(self, ball, board, bricks) -> None:
        """Initialize the parameters for the model class."""
        self.ball = ball
        self.board = board
        self.bricks = bricks
        
    def tick(self) -> None:
        """Updates the model every fractional second."""
        self.time += 1
        self.ball.tick()
        self.enforce_bounds_ball()        
        
        
    def enforce_bounds_ball(self) -> None:
        """Ensures that the ball does not escape the box."""
        ball_x: int = self.ball.x
        ball_y: int = self.ball.y
        board_x: int = self.board.x
        board_y: int = self.board.y
        
        # Check contact with the Bricks.
        for brick in self.bricks:
            if (brick.x <= ball_x <= brick.x + BRICK_LENGTH 
                and ((brick.y - LAMDA <= ball_y <= brick.y + LAMDA) 
                     or (brick.y - LAMDA - BRICK_HEIGHT <= ball_y + BALL_RADIUS <= brick.y + LAMDA - BRICK_HEIGHT))):
                self.ball.change_directions(Vector(self.ball.vector.x_vector, -1 * self.ball.vector.y_vector))
                brick.hit_brick()
                if brick.is_dead():
                    self.bricks.remove(brick)
                    if brick.type == "two":
                        self.ball.change_directions(Vector(0.5 * self.ball.vector.x_vector, 0.5 * self.ball.vector.y_vector))
                    elif brick.type == "three":
                        self.ball.change_directions(Vector(2 * self.ball.vector.x_vector, 2 * self.ball.vector.y_vector))
                    
            elif (brick.y - BRICK_HEIGHT <= ball_y <= brick.y 
                and ((ball_x - LAMDA <= brick.x <= ball_x + LAMDA) 
                     or (ball_x - LAMDA <= brick.x + BRICK_LENGTH <= ball_x + LAMDA))):
                self.ball.change_directions(Vector(-1 * self.ball.vector.x_vector, self.ball.vector.y_vector))
                brick.hit_brick()
                if brick.is_dead():
                    self.bricks.remove(brick)
                    if brick.type == "two":
                        self.ball.change_directions(Vector(0.5 * self.ball.vector.x_vector, 0.5 * self.ball.vector.y_vector))
                    elif brick.type == "three":
                        self.ball.change_directions(Vector(2 * self.ball.vector.x_vector, 2 * self.ball.vector.y_vector))
        
        # Check contact with Board.
        if (board_y - 5 < ball_y - BALL_RADIUS <= board_y 
            and board_x - BOARD_LENGTH < ball_x <= board_x + BOARD_LENGTH):
            self.ball.change_directions(Vector(self.ball.vector.x_vector, -1 * self.ball.vector.y_vector))
            
        # Check contact with left and right side.
        if (ball_x + BALL_RADIUS) >= MAX_X or (ball_x - BALL_RADIUS) <= -MAX_X:
            self.ball.change_directions(Vector(-1 * self.ball.vector.x_vector, self.ball.vector.y_vector))
        
        # Check contatc with top and bottom side.
        if (ball_y + BALL_RADIUS) >= MAX_Y:
            self.ball.change_directions(Vector(self.ball.vector.x_vector, -1 * self.ball.vector.y_vector))
            
    def game_over(self) -> bool:
        """Checks to see if the game is over."""
        return True if (self.ball.y + BALL_RADIUS <= -MAX_Y) or len(self.bricks) == 0 else False