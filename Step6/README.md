# Step 6: Enemies & Collision

Now it's time to bring some interaction to our game. For the obstacle we add again a new class.
```
class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [pygame.image.load("cactus1.png"), pygame.image.load("cactus2.png"),
                       pygame.image.load("cactus3.png"), pygame.image.load("cactus4.png"),
                       pygame.image.load("cactus5.png")]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
```

We position the obstacles also randomly in the game, so we add another positionlist just like we did for the clouds.
```
cloud_position_list = []
cactus_position_list = []
for i in range(100):
    x = random.randrange(0, 50000, 50)
    y = random.randrange(75, 150, 25)
    cloud_position_list.append([x, y])
    x = random.randrange(100, 50000)
    cactus_position_list.append([x, 0, 23])
```

In our level-constructor we also add the obstacles.
```
def __init__(self, score, font):
    ...
    self.cactus_list = pygame.sprite.Group()
    ...
    for position in cactus_position_list:
        cactus = Cactus()
        cactus.image = cactus.images[random.randrange(0, 4)]
        cactus.rect.x = position[0]
        cactus.rect.y = SCREEN_HEIGHT - cactus.image.get_rect().height
        self.cactus_list.add(cactus
```

And don't forget to adjust our draw- and worldshift-methods.
```
def draw(self, screen):
    ...
    self.cactus_list.draw(screen)

def shift_world(self, shift_x):
    ...
    for cactus in self.cactus_list:
        cactus.rect.x += shift_x
```

Now we have to add the behaviour for the collision. Therefore the player needs a new attribute. We also add a boolean attribute to check if the game is over.
```
def __init__(self, level):
    super().__init__()
    ...
    self.level = level
    self.gameover = False
```

The collision detection itself will be in the update-method. Spritecollide checks if the player is at the same position as an object of the levels obstacles. If this is the case we set gameover to true.
```
def update(self):
    ...
    block_hit_list = pygame.sprite.spritecollide(self, self.level.cactus_list, False)
    for _ in block_hit_list:
        self.stop()
        self.gameover = True
```

In our main-method the player will be initialized with our level and we adjust our main loop, so that the program will stop when the player hits one of the obstacles.
```
level = Level(0, font)
player = Player(level)
...
while not done and not player.gameover:
    ...
```

That's it. Run with `python trex_runner.py`