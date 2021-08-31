from turtle import Turtle


class Tab(Turtle):
#Tab hereda de la clase Turtle
    def __init__(self, side):
        super().__init__()
        #Dentro del constructor he puesto super para que pueda heredar
        # en el mismo constructor y no tener que instanciar
        """Crea una barra de lado izquierdo o derecho"""
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        if side == "right":
            self.setpos(x=350, y=0)
        else:
            self.setpos(x=-350, y=0)


    def go_up(self):
        """Desplaza hacía abajo. Reemplaza las coordenadas de y anteriores y les suma 20, x se mantiene igual"""

        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def go_down(self):
        """Desplaza hacía abajo. Reemplaza las coordenadas de y anteriores y les resta 20, x se mantiene igual"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)





