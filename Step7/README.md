# Step 7: Spritesheets

We are really far now with our game. But it would look even better, if our T-Rex was animated. Therefor we will use spritesheets.
We use a class from [this example](http://programarcadegames.com/python_examples/en/sprite_sheets/) which gets a part out of an image with given coordinates. This way we can use a spritesheet with several images.
Put this class in the same folder where trex_runner.py is. Next we have to import this class.
```
from spritesheet_functions import SpriteSheet
```

Our spritesheet for the T-Rex will be "trexrun.png". There are 3 different T-Rex which we will append to an imagearray in our constructor. Defaultimage will be the first T-Rex.
Also add the last line to jump() and stop(), because we want no moving T-Rex during standing or jumping.
```
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
    ...
```

To switch the T-Rex image during running we randomly pick one of the given images in the update-method.
```
if self.x != 0 and self.y == 0:
    self.image = self.images[random.randrange(0, 3)]
```

We have a running T-Rex now an we can throw away the trex.png. But there are still a lot of images in our folder. So let's also use Spritesheets for the other objects and delete the obsolete images.
```
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
```

Still there is a lot of code in our trex_runner.py and as our game maybe will even grow the code could get confusing with the time. Just as we imported the spritesheet we can split up our module and import them again.
I extracted the player-class to an own module and cloud, cactus, floor and level to another one, so we only have the main method in our trex_runner.py.
That's all for now, we're at the end of our tutorial. Feel free to add other objects and functions. There is a todo-list in the main README if you have no more ideas ;)