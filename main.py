import pygame
from ball import Ball
from paddle import Paddle

WIDTH = 1000
HEIGHT = 600

BALL_RADIUS = 16

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 120

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
game_over = False

pygame.display.set_caption("Pong")
icon = pygame.image.load("Images/pong.png")
pygame.display.set_icon(icon)

ball = Ball(screen, (WIDTH / 2) - BALL_RADIUS, (HEIGHT / 2) - BALL_RADIUS)
left_paddle = Paddle(screen, (100 - PADDLE_WIDTH / 2), (HEIGHT / 2) - (PADDLE_HEIGHT / 2))
right_paddle = Paddle(screen, (WIDTH - (100 - PADDLE_WIDTH / 2)), (HEIGHT / 2) - (PADDLE_HEIGHT / 2))

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.update()
    left_paddle.update()
    right_paddle.update()
    pygame.display.update()
