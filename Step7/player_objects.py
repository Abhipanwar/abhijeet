import pygame
import random
from spritesheet_functions import SpriteSheet

SCREEN_HEIGHT = 300


class Player(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.images = []

        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("trexrun.png")

        image = sprite_sheet.get_image(0, 0, 40, 48)
        self.images.append(image)
        image = sprite_sheet.get_image(0, 48, 40, 48)
        self.images.append(image)
        image = sprite_sheet.get_image(0, 96, 40, 48)
        self.images.append(image)

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.level = level
        self.gameover = False

    def update(self):
        self.calc_grav()
        self.rect.x += self.x
        self.rect.y += self.y

        if self.x != 0 and self.y == 0:
            self.image = self.images[random.randrange(0, 3)]

        block_hit_list = pygame.sprite.spritecollide(self, self.level.cactus_list, False)
        for _ in block_hit_list:
            self.stop()
            self.gameover = True

    def calc_grav(self):
        if self.y != 0:
            self.y += .35

        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.y >= 0:
            self.y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        if self.y == 0:
            self.y -= 10
            self.image = self.images[0]

    def move_right(self):
        self.x = 10

    def stop(self):
        self.x = 0
        self.image = self.images[0]
