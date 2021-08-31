from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        #self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.shape("circle")
        self.color("red")
        self.setpos(0,0)
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_fromTD(self):
        """Hace negativo el valor al que se trasladará la bola en el eje y"""
        self.y_move *= -1

    def bounce_on_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball_pos(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_on_x()
        self.bounce_fromTD()
