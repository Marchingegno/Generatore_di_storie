from PIL import Image, ImageDraw, ImageFont


def writeinimage(imagePath, x, y, text, size=100):
    image = Image.open(imagePath)
    font = ImageFont.truetype("22815_LCOUR.ttf", size)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(x, y), text=text, fill=(255, 255, 255), font=font)
    image.show()


writeinimage('pic.jpg', 250, 250, "ciaooo", 300)
