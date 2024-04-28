from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.text = None
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Bodies: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.update_score()
