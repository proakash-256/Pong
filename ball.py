import pygame

WIDTH = 1000
HEIGHT = 600
RADIUS = 16


class Ball:
    def __init__(self, screen, xcor, ycor):
        self.screen = screen
        self.ball_img = pygame.image.load("Images/ball.png")
        self.xcor = xcor
        self.ycor = ycor

    def update(self):
        self.screen.blit(self.ball_img, (self.xcor, self.ycor))
