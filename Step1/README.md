# Step 1: Open a window

First of all, we need to import pygame and initialize it
```
import pygame
pygame.init()
```

Next we define some variables
```
WHITE = (255, 255, 255)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 300
```

Now we can set the screen, open our window and give it a title.
```
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("T-Rex Runner")
```

After that we have our main program loop. The loop runs as long, as the user will not click the close button. We fill our screen with our predefined color (`screen.fill(WHITE)`) and then update the screen with what we've drawn (`pygame.display.flip()`).
`clock.tick(60)` will limit the loop to a maximum of 60 times per second. If we leave it empty, we will use all CPU we can.
```
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(60)
```

Finally we close our window and quit
```
pygame.quit()
```

Run with `python trex_runner.py`