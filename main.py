import pygame
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

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

player1_scoreboard = Scoreboard(screen, "Player1", 25, 25)
player2_scoreboard = Scoreboard(screen, "Player2", 825, 25)

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                right_paddle.vel = -0.9
            if event.key == pygame.K_DOWN:
                right_paddle.vel = 0.9

            if event.key == pygame.K_w:
                left_paddle.vel = -0.9
            if event.key == pygame.K_s:
                left_paddle.vel = 0.9

        if event.type == pygame.KEYUP:
            left_paddle.vel = 0
            right_paddle.vel = 0

    # Ball Bounce Control
    if (ball.ycor <= 0 + BALL_RADIUS) or (ball.ycor >= HEIGHT - BALL_RADIUS):
        ball.yvel *= -1

    if ball.xcor >= WIDTH - BALL_RADIUS:
        player1_scoreboard.score += 1
        ball.xcor = (WIDTH / 2) - BALL_RADIUS
        ball.ycor = (HEIGHT / 2) - BALL_RADIUS
        ball.xvel *= -1
        ball.yvel *= -1

    if ball.xcor <= 0 + BALL_RADIUS:
        player2_scoreboard.score += 1
        ball.xcor = (WIDTH / 2) - BALL_RADIUS
        ball.ycor = (HEIGHT / 2) - BALL_RADIUS
        ball.xvel = 0.5
        ball.yvel = 0.5

    left_paddle.control()
    right_paddle.control()

    left_paddle.ycor += left_paddle.vel
    right_paddle.ycor += right_paddle.vel

    # Collision Detection
    if left_paddle.xcor <= ball.xcor <= left_paddle.xcor + PADDLE_WIDTH:
        if left_paddle.ycor <= ball.ycor <= left_paddle.ycor + PADDLE_HEIGHT:
            ball.xcor = left_paddle.xcor + PADDLE_WIDTH
            ball.xvel *= -1

    if right_paddle.xcor <= ball.xcor <= right_paddle.xcor + PADDLE_WIDTH:
        if right_paddle.ycor <= ball.ycor <= right_paddle.ycor + PADDLE_HEIGHT:
            ball.xcor = right_paddle.xcor
            ball.xvel *= -1

    ball.xcor += ball.xvel
    ball.ycor += ball.yvel

    ball.update()
    left_paddle.update()
    right_paddle.update()
    player1_scoreboard.update()
    player2_scoreboard.update()

    winning_font = pygame.font.SysFont("callibri", 100)
    if player1_scoreboard.score >= 11:
        screen.fill((0, 0, 0))
        end_screen = winning_font.render("Player1 Won!!", True, (255, 255, 255))
        screen.blit(end_screen, (200, 250))
    if player2_scoreboard.score >= 11:
        screen.fill((0, 0, 0))
        end_screen = winning_font.render("Player2 Won!!", True, (255, 255, 255))
        screen.blit(end_screen, (200, 250))

    pygame.display.update()
