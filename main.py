import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
running = True
game_over = False

pygame.display.set_caption("Pong")
icon = pygame.image.load("Images/pong.png")
pygame.display.set_icon(icon)

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
