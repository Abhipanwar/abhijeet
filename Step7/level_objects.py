import pygame
import random
from spritesheet_functions import SpriteSheet

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_HEIGHT = 300

cloud_position_list = []
cactus_position_list = []
for i in range(100):
    x = random.randrange(0, 50000, 50)
    y = random.randrange(75, 150, 25)
    cloud_position_list.append([x, y])
    x = random.randrange(100, 50000, 23)
    cactus_position_list.append([x, 0])


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cloud.png").convert()
        self.rect = self.image.get_rect()


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []

        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("floor.png")

        image = sprite_sheet.get_image(0, 0, 30, 15)
        self.images.append(image)
        image = sprite_sheet.get_image(0, 15, 30, 15)
        self.images.append(image)
        image = sprite_sheet.get_image(0, 30, 30, 15)
        self.images.append(image)
        image = sprite_sheet.get_image(0, 45, 30, 15)
        self.images.append(image)
        image = sprite_sheet.get_image(0, 60, 30, 15)
        self.images.append(image)

        self.image = self.images[0]
        self.rect = self.image.get_rect()


class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []

        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("cactus.png")

        image = sprite_sheet.get_image(0, 0, 15, 38)
        self.images.append(image)
        image = sprite_sheet.get_image(0, 38, 22, 52)
        self.images.append(image)
        image = sprite_sheet.get_image(0, 90, 17, 50)
        self.images.append(image)
        image = sprite_sheet.get_image(0, 140, 13, 33)
        self.images.append(image)
        image = sprite_sheet.get_image(0, 173, 23, 52)
        self.images.append(image)

        self.image = self.images[0]
        self.rect = self.image.get_rect()


class Level(pygame.sprite.Sprite):
    def __init__(self, score, font):
        super().__init__()
        self.score = score
        self.font = font
        self.cloud_list = pygame.sprite.Group()
        self.floor_list = pygame.sprite.Group()
        self.cactus_list = pygame.sprite.Group()
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

        for position in cactus_position_list:
            cactus = Cactus()
            cactus.image = cactus.images[random.randrange(0, 4)]
            cactus.rect.x = position[0]
            cactus.rect.y = SCREEN_HEIGHT - cactus.image.get_rect().height
            self.cactus_list.add(cactus)

    def update(self):
        self.score += 0.1

    def draw(self, screen):
        screen.fill(WHITE)
        self.cloud_list.draw(screen)
        self.floor_list.draw(screen)
        self.cactus_list.draw(screen)
        label = self.font.render("Score: " + str(int(self.score)).zfill(4), 1, BLACK)
        screen.blit(label, (850, 10))

    def shift_world(self, shift_x):
        self.world_shift += shift_x
        for cloud in self.cloud_list:
            cloud.rect.x += shift_x
        for floor in self.floor_list:
            floor.rect.x += shift_x
        for cactus in self.cactus_list:
            cactus.rect.x += shift_x
