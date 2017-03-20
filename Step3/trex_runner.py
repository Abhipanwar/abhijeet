import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 300


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("trex.png")
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

    def update(self):
        self.rect.x += self.x
        self.rect.y += self.y

    def jump(self):
        self.y -= 1

    def move_right(self):
        self.x = 1


def main():
    pygame.init()

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("T-Rex Runner")

    done = False
    clock = pygame.time.Clock()

    player = Player()
    player.rect.x = 5
    player.rect.y = SCREEN_HEIGHT - player.rect.height

    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(player)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(WHITE)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_UP:
                player.jump()

        active_sprite_list.update()
        active_sprite_list.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
