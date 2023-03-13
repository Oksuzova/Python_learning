from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 190)
        self.write(f"{self.l_score} {self.r_score}", align="center", font=('Courier', 80, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.write(f"{self.l_score} {self.r_score}", align="center", font=('Courier', 80, 'normal'))

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.write(f"{self.l_score} {self.r_score}", align="center", font=('Courier', 80, 'normal'))
