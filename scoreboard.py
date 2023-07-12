from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
MOVE = False


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.goto(0, 265)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt") as file:
            content = int(file.read())
            return content

    def update_high_score(self, new_high_score):
        with open("data.txt", mode="w") as file:
            file.write(str(new_high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", MOVE, ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.update_high_score(self.score)
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over.", align=ALIGNMENT, font=FONT)
