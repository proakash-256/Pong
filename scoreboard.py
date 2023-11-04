import pygame


class Scoreboard:
    def __init__(self, screen, name, xcor, ycor):
        self.screen = screen
        self.name = name
        self.score = 0
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.xcor = xcor
        self.ycor = ycor

    def update(self):
        score_text = self.font.render(f"{self.name}: {str(self.score)}", True, (255, 255, 255))
        self.screen.blit(score_text, (self.xcor, self.ycor))
