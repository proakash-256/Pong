import pygame

WIDTH = 1000
HEIGHT = 600

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 120

class Paddle:
    def __init__(self, screen, xcor, ycor):
        self.screen = screen
        self.paddle_img = pygame.image.load("Images/paddle.png")
        self.xcor = xcor
        self.ycor = ycor
        self.vel = 0

    def control(self):
        if self.ycor >= HEIGHT - PADDLE_HEIGHT:
            self.ycor = HEIGHT - PADDLE_HEIGHT

        if self.ycor <= 0:
            self.ycor = 0

    def update(self):
        self.screen.blit(self.paddle_img, (self.xcor, self.ycor))
