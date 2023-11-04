import pygame

class Paddle:
    def __init__(self, screen, xcor, ycor):
        self.screen = screen
        self.paddle_img = pygame.image.load("Images/paddle.png")
        self.xcor = xcor
        self.ycor = ycor

    def update(self):
        self.screen.blit(self.paddle_img, (self.xcor, self.ycor))
