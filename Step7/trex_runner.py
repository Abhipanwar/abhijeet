import pygame
from level_objects import Level
from player_objects import Player

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 300


def main():
    pygame.init()
    font = pygame.font.SysFont("monospace", 15)

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("T-Rex Runner")

    done = False
    clock = pygame.time.Clock()

    level = Level(0, font)
    player = Player(level)
    player.rect.x = 5
    player.rect.y = SCREEN_HEIGHT - player.rect.height

    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(player)

    while not done and not player.gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_UP:
                player.jump()

        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_RIGHT and player.x > 0:
        #         player.stop()

        if player.x != 0:
            level.update()
        active_sprite_list.update()

        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            level.shift_world(-diff)

        level.draw(screen)
        active_sprite_list.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
