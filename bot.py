import random
import time
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler

import bot_secred_token
import constants


def writeinimage(imagePath, x, y, text, size=70):
    image = Image.open(imagePath)
    font = ImageFont.truetype("22815_LCOUR.ttf", size)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(x, y), text=text, fill=(255, 255, 255), font=font)
    return image


def getrandomstory():
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
    return writeinimage(randpic, randx, randy, randtext, size=randsize)


def randomstory(bot, update):
    image = getrandomstory()
    print("Requested story: " + time.time().__str__())
    bio = BytesIO()
    bio.name = 'image.jpeg'
    image.save(bio, 'JPEG')
    bio.seek(0)
    chat_id = update.message.chat_id
    menukeyboard = [['/randomstory']]
    menumarkup = ReplyKeyboardMarkup(menukeyboard, one_time_keyboard=True, resize_keyboard=True)
    bot.send_photo(chat_id=chat_id, photo=bio, reply_markup=menumarkup)


def main():
    updater = Updater(bot_secred_token.token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('randomstory', randomstory))
    print("added handler")
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
