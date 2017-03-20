import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 300

pygame.init()

size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("T-Rex Runner")

done = False
clock = pygame.time.Clock()

player = pygame.Surface([40, 40])
player.fill(BLACK)
x = 100
y = 100

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            x += 1
        if event.key == pygame.K_UP:
            y -= 1

    screen.blit(player, [x, y])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
