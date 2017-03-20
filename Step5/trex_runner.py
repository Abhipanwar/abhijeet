import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 300

cloud_position_list = []
for i in range(100):
    x = random.randrange(0, 50000, 50)
    y = random.randrange(75, 150, 25)
    cloud_position_list.append([x, y])


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("trex.png")
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

    def update(self):
        self.calc_grav()
        self.rect.x += self.x
        self.rect.y += self.y

    def calc_grav(self):
        if self.y != 0:
            self.y += .35

        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.y >= 0:
            self.y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        if self.y == 0:
            self.y -= 10

    def move_right(self):
        self.x = 10

    def stop(self):
        self.x = 0


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cloud.png").convert()
        self.rect = self.image.get_rect()


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [pygame.image.load("floor1.png"), pygame.image.load("floor2.png"),
                       pygame.image.load("floor3.png"), pygame.image.load("floor4.png"),
                       pygame.image.load("floor5.png")]
        self.image = self.images[0]
        self.rect = self.image.get_rect()


class Level(pygame.sprite.Sprite):
    def __init__(self, score, font):
        super().__init__()
        self.score = score
        self.font = font
        self.cloud_list = pygame.sprite.Group()
        self.floor_list = pygame.sprite.Group()
        self.world_shift = 0

        for position in cloud_position_list:
            cloud = Cloud()
            cloud.rect.x = position[0]
            cloud.rect.y = position[1]
            self.cloud_list.add(cloud)

        pos = 0
        for _ in range(0, 1700):
            floor = Floor()
            floor.rect.x = pos
            floor.rect.y = SCREEN_HEIGHT - floor.image.get_rect().height
            floor.image = floor.images[random.randrange(0, 4)]
            self.floor_list.add(floor)
            pos += 30

    def update(self):
        self.score += 0.1

    def draw(self, screen):
        screen.fill(WHITE)
        self.cloud_list.draw(screen)
        self.floor_list.draw(screen)
        label = self.font.render("Score: " + str(int(self.score)).zfill(4), 1, BLACK)
        screen.blit(label, (850, 10))

    def shift_world(self, shift_x):
        self.world_shift += shift_x
        for cloud in self.cloud_list:
            cloud.rect.x += shift_x
        for floor in self.floor_list:
            floor.rect.x += shift_x


def main():
    pygame.init()
    font = pygame.font.SysFont("monospace", 15)

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("T-Rex Runner")

    done = False
    clock = pygame.time.Clock()

    level = Level(0, font)
    player = Player()
    player.rect.x = 5
    player.rect.y = SCREEN_HEIGHT - player.rect.height

    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.add(player)

    while not done:
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
