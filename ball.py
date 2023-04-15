from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.shapesize(2, 2)
        self.speed("slow")
        self.penup()
        self.xcor_move = 0.5
        self.ycor_move = 0.5



    def move(self):
        new_x = self.xcor() + self.xcor_move
        new_y = self.ycor() + self.ycor_move

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ycor_move *= -1

    def bounce_x(self):
        self.xcor_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

    # def reset_position(self):
    #     self.goto(0, 0)
    #     self.bounce_x()






