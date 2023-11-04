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

    def bounce_control(self):
        if (self.ycor <= 0 + BALL_RADIUS) or (self.ycor >= HEIGHT - BALL_RADIUS):
            self.yvel *= -1

        if self.xcor >= WIDTH - BALL_RADIUS:
            self.xcor = (WIDTH / 2) - BALL_RADIUS
            self.ycor = (HEIGHT / 2) - BALL_RADIUS
            self.xvel *= -1
            self.yvel *= -1

        if self.xcor <= 0 + BALL_RADIUS:
            self.xcor = (WIDTH / 2) - BALL_RADIUS
            self.ycor = (HEIGHT / 2) - BALL_RADIUS
            self.xvel = 0.5
            self.yvel = 0.5

    def update(self):
        self.screen.blit(self.ball_img, (self.xcor, self.ycor))
