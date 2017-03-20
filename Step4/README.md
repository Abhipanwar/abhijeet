# Step 4: Add some more methods for the player

At the moment our T-Rex does not come back down, after jumping, so we need to add some kind of gravity.
So let's add a method for that in our class Player(), which does the following: if there is a change in y-direction we add 0,35 to our change (remember the reversed y-axis) and if we reach the bottom, we set the change to 0.
```
def calc_grav(self):
    if self.y != 0:
        self.y += .35

    if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.y >= 0:
        self.y = 0
        self.rect.y = SCREEN_HEIGHT - self.rect.height
```

Then we need to adjust the update-Method:
```
def update(self):
    self.calc_grav()
    self.rect.x += self.x
    self.rect.y += self.y
```

At the moment we can jump even if we are in the air, so let's stop this behaviour.
```
def jump(self):
    if self.y == 0:
        self.y -= 10
```

We move a bit slow, so let's speed up a bit.
```
def move_right(self):
    self.x = 10
```

We don't need any stop-methods or anything like that for the T-Rex Runner, but I want to show, how this would be done. First we need another method in our class Player().
```
def stop(self):
    self.x = 0
```

We want to call this method, when we stop pressing the arrow buttons. So we have to call it in another event loop in our main program loop.
```
if event.type == pygame.KEYUP:
    if event.key == pygame.K_RIGHT and player.x > 0:
        player.stop()
```

Now we can also stop, if we want to. But as we don't need it in the future, we can take this part out again (I commented it out in the code.) Run the program as usual with `python trex_runner.py`