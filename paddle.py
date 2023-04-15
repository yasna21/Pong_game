from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # Set up first paddle

        self.shape("square")
        self.penup()
        self.shapesize(7, 1)
        self.color("white")
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
