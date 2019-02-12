# pythonchallenge 11
# 5808.html

from PIL import Image, ImageDraw

image = Image.open('ingredient/cave.jpg')
new = Image.new('RGB', (640, 480))

for i in range(image.height):
    for j in range(image.width):
        if i % 2 == 1 and j % 2 == 1:
            new.putpixel((j, i), image.getpixel((j, i)))

new.show()
