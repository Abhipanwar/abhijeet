# Step 3: Methods & Classes

As our trex_runner.py becomes bigger, we should clean up a bit. Usually you use several python-modules and include them by imports.
To check, if our code is being imported or run we can use a global variable defined automatically by Python.
This global variable is called `__name__`. We wrap now our code into a method called 'main' and call it if our code is being run.
```
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 300


def main():
    pygame.init()
    ...
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    ...
    pygame.quit()

if __name__ == "__main__":
    main()
```

Now it's time to add a class for our player. As it will interact with other objects in our game, we need a collision detection.
The pygame library has support for sprites, which we will use for all of our objects in the game now.
Add the class Player above the main-function. It has the parent class Sprite and we also have a constructor method (`def __init__(self)`) in which we call the parent (`super().__init__()`).
As we want our player to be a T-Rex we use an image for that. We use a rectangle and some coordinates to position our player image in our window.
```
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("trex.png")
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
```

We need some methods to move the player. In our class Player we add the methods update() which we will call after there was some input by the user, jump() to move upwards and move_right() to move to the right.
```
def update(self):
    self.rect.x += self.x
    self.rect.y += self.y

def jump(self):
    self.y -= 1

def move_right(self):
    self.x = 1
```

Next we need to initialize our player in the main-method. If you haven't already, delete the following lines...
```
player = pygame.Surface([40, 40])
player.fill(BLACK)
x = 100
y = 100
```

...and replace them by:
```
player = Player()
player.rect.x = 5
player.rect.y = SCREEN_HEIGHT - player.rect.height

active_sprite_list = pygame.sprite.Group()
active_sprite_list.add(player)
```

Pygame.sprite.Group() is a container class to hold and manage multiple Sprite objects.
We also need to change our event loop and call our methods from class Player() here.
```
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_RIGHT:
        player.move_right()
    if event.key == pygame.K_UP:
        player.jump()
```

Last, we have to add the update-Method call right before the flip() Method and then 'draw' our player to the screen. Draw is a method from sprite.Group.
```
active_sprite_list.update()
active_sprite_list.draw(screen)
```

Run with `python trex_runner.py`