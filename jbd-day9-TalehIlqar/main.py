from os import write
from PIL import Image, ImageFont, ImageDraw 
import requests


def responce():
    responce = requests.get('https://memegenerator.net/img/instances/400x/56565615/coders-gonna-code.jpg')
    with open("responce.jpg", "wb") as f:
        f.write(responce.content)
responce()

im1 = Image.open('responce.jpg')
im1.save('responce.png')
print(im1)

# im1.show()


fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 50)
title_text = "Tech Academy"
image_editable = ImageDraw.Draw(im1)
image_editable.text((0,90), title_text, (237, 230, 211), font = fnt)

im1.save("result.jpg")
im1.show()  