"""The main code for the visual aspect of the GUI."""

from turtle import Screen, Turtle, done
from typing import Any
from constants import BOARD_LENGTH, BRICK_HEIGHT, BRICK_LENGTH, MAX_X, MAX_Y
from model.model import Model
from time import time_ns

NS_TO_MS: int = 1000000

class ViewController:
    """Represents the display screen."""
    screen: Any
    pen: Turtle
    model: Model
    
    def __init__(self, model) -> None:
        """Constructor for the View Controller."""
        self.model = model
        self.screen = Screen()
        self.screen.setup(MAX_X * 2, MAX_Y * 2)
        self.screen.tracer(0, 0)
        self.screen.delay(0)
        self.screen.title("Brick Breaker :)")
        self.screen.bgcolor("black")
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.speed(0) 
        
    def start_simulation(self) -> None:
        """Started the turtle gfx."""
        self.tick()
        done()
        
    def tick(self) -> None:
        """Updates the model and redraws the visuals."""
        start_time = time_ns() // NS_TO_MS
        self.model.tick()
        self.screen.listen()
        self.screen.onkey(self.model.board.move_left, "Left")
        self.screen.onkey(self.model.board.move_left, "h")
        self.screen.onkey(self.model.board.move_right, "Right")
        self.screen.onkey(self.model.board.move_right, "l")
        self.pen.clear()
        
        # Draw the Ball.
        self.pen.penup()
        self.pen.goto(self.model.ball.x, self.model.ball.y)
        self.pen.pendown()
        self.pen.pencolor("white")
        self.pen.dot(self.model.ball.radius, "white")
        
        # Draw the Board.
        self.pen.penup()
        self.pen.goto(self.model.board.x - 0.5 * BOARD_LENGTH, self.model.board.y)
        self.pen.pendown()
        self.pen.setheading(0)
        self.pen.pencolor("red")
        self.pen.color("red")
        self.pen.begin_fill()
        self.pen.forward(BOARD_LENGTH)
        self.pen.right(90)
        self.pen.forward(5)
        self.pen.right(90)
        self.pen.forward(BOARD_LENGTH)
        self.pen.right(90)
        self.pen.forward(5) 
        self.pen.end_fill()     
        
        # TODO: Draw the Bricks.
        for brick in self.model.bricks:
            self.pen.penup()
            self.pen.goto(brick.x, brick.y)
            self.pen.setheading(0)
            self.pen.color(brick.color)
            self.pen.begin_fill()
            self.pen.forward(BRICK_LENGTH)
            self.pen.right(90)
            self.pen.forward(BRICK_HEIGHT)
            self.pen.right(90)
            self.pen.forward(BRICK_LENGTH)
            self.pen.right(90)
            self.pen.forward(BRICK_HEIGHT)
            self.pen.end_fill()
                
        self.screen.update()
        
        if not self.model.game_over():
            end_time = time_ns() // NS_TO_MS
            next_tick = 30 - (end_time - start_time)
            if next_tick < 0:
                next_tick = 0
                
            self.screen.ontimer(self.tick, next_tick)
        else:
            self.pen.clear()
            self.pen.goto(0, 0)
            self.pen.write("GAME OVER", move=True, align="center", font=('Arial', 24, 'normal'))