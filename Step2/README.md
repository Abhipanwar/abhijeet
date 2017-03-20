# Step 2: Add a player and navigate it trough the window

We define now another color and our player. x and y defines our position in our window. You can imagine our window as coordinate system with a reversed y-axis.
pygame.Surface is a pygame object, which represents an image.
```
BLACK = (0, 0, 0)
player = pygame.Surface([40, 40])
player.fill(BLACK)
x = 100
y = 100
```

In our main program loop we add our player by drawing our player image on the screen.
```
screen.blit(player, [x, y])
```

To navigate our player we need to react on the users input. If the user presses right arrow we want to move to the right, if the user presses up arrow we want to move to the top.
So in our main loop we add the following event loop. Depending on the users input we change our coordinates. Remember that the y-axis is reversed, so we have to subtract here to move upwards.
```
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_RIGHT:
        x += 1
    if event.key == pygame.K_UP:
        y -= 1
```

Run with `python trex_runner.py`