# Step 5: Add Level and worldshift

At the moment we can't see where our T-Rex is going after leaving the window on the right, so we need a worldshift to the right.
Later we want some background and enemies who interact with the player. So we add a new class Level, also with parent Strite. The initial world shift is 0 and if we call the method to shift world it will be increased.
We also need a draw method to fill the background.
```
class Level(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.world_shift = 0

    def draw(self, screen):
        screen.fill(WHITE)

    def shift_world(self, shift_x):
        self.world_shift += shift_x
```

The level should get initialized in our main method.
```
level = Level()
```

In the main loop we call the worldshift-Method if the player reaches the middle of the screen. Call the draw-Method right before we draw the player.
```
if player.rect.right >= 500:
    diff = player.rect.right - 500
    player.rect.right = 500
    level.shift_world(-diff)

level.draw(screen)
```

Time to draw something in our level. How about a score on the right top? For a score we init a font and we also need to change our Level()-constuctor where we hand over a score and the font.
```
font = pygame.font.SysFont("monospace", 15)
level = Level(0, font)
```

In our constuctor we should init our new attributes.
```
def __init__(self, score, font):
    ...
    self.score = score
    self.font = font
    ...
```

We increase the score in a nwe method. Call this update-Method in the main-Method right before you update the player.
In the draw-Method we put our score on the screen. We use a label for that. Zfill(4) will ensure the score is filled up with leading zeros, if the score is low.
```
def update(self):
    self.score += 0.1

def draw(self, screen):
    screen.fill(WHITE)
    label = self.font.render("Score: " + str(int(self.score)).zfill(4), 1, BLACK)
    screen.blit(label, (850, 10))
```

To only start the score updating after we started to run, we should add a check, if the player is running already.
```
if player.x != 0:
    level.update()
```

Next let's add some background. In the T-Rex Runner there should be some clouds and a floor. We will use a new class for both of them.
```
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
```

We want to appear the clouds randomly on the screen. So we will build an array of different positions for the clouds. I added a step of 50 and 25 for width and height, so that there are no clouds overlapping.
```
import random

cloud_position_list = []
for i in range(100):
    x = random.randrange(0, 50000, 50)
    y = random.randrange(75, 150, 25)
    cloud_position_list.append([x, y])
```

Back in the Level class we need to update our constructor. Just as we did with our player in the main program loop we init now the clouds and floor as a sprite group.
In the first loop we add a cloud for each position we have in our predefined cloud_position_list. In the second loop we randomly pick a floor-image every 30 steps on our x-axis.
```
def __init__(self, score, font):
    ...
    self.cloud_list = pygame.sprite.Group()
    self.floor_list = pygame.sprite.Group()

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
```

To paint the clouds and floor on the screen we have to add the following lines in the draw-Method.
```
self.cloud_list.draw(screen)
self.floor_list.draw(screen)
```

And the last step ist to shift the background when the world is shifting. So we add in shift_world:
```
for cloud in self.cloud_list:
    cloud.rect.x += shift_x
for floor in self.floor_list:
    floor.rect.x += shift_x
```

We're ready. In the next step we will add some enemies and collision. But for now, run the program with `python trex_runner.py`