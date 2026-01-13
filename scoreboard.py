from food import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        with open("high_score.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 20, "normal"))


    def add_point(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score>self.highscore:
            self.highscore = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()




