import pygame

BALL_RADIUS = 16
WIDTH = 1000
HEIGHT = 600


class Ball:
    def __init__(self, screen, xcor, ycor):
        self.screen = screen
        self.ball_img = pygame.image.load("Images/ball.png")
        self.xcor = xcor
        self.ycor = ycor
        self.xvel = 0.5
        self.yvel = 0.5

    def update(self):
        self.screen.blit(self.ball_img, (self.xcor, self.ycor))
