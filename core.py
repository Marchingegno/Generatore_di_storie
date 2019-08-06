import random

from PIL import Image, ImageDraw, ImageFont

import constants


def writeinimage(imagePath, x, y, text, size=70):
    image = Image.open(imagePath)
    font = ImageFont.truetype("22815_LCOUR.ttf", size)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(x, y), text=text, fill=(255, 255, 255), font=font)
    image.show()


randsize = random.randint(constants.MINSIZE, constants.MAXSIZE)
randx = random.randint(constants.MINX, constants.MAXX)
randy = random.randint(constants.MINY, constants.MAXY)
while 1700 > randy > 1400:
    # this avoids putting the text in the middle of the buttons
    randy = random.randint(constants.MINY, constants.MAXY)

lines = open('phrases.txt').read().splitlines()
randtext = random.choice(lines)

randpicnumber = random.randint(1, constants.PICNUMBER)
randpic = "images/pic (@).png"
randpic = randpic.replace("@", randpicnumber.__str__())
writeinimage(randpic, randx, randy, randtext, size=randsize)

print(randx, randy)
