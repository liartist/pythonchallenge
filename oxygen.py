# pythonchallenge 7
# oxygen.html

from PIL import Image

image = Image.open('ingredient/oxygen.png')
rgb = image.convert('RGB')
answer = ''
x = 0

for i in range(image.height):
    for j in range(image.width):
        r, g, b = rgb.getpixel((j, i))
        if i == int(image.height / 2) and r == g == b:
            if x != r:
                answer += str(chr(r))
                x = r

print(answer)
answer = answer.split('[')[1]
answer = answer.split(']')[0]
answers = answer.split(', ')

for a in answers:
    print(str(chr(int(a))), end=' ')
