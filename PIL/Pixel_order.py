from PIL import Image

img = Image.open('doggo.png')
pixels = []
bright = []
sort = []
final = []

def sorter(a):
    return a[3]

for x in range(img.width):
    for y in range(img.height):
        pixels.append(img.getpixel((x,y)))

for pixel in pixels:
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    avg = round((r + g + b)/3,0)

    bright.append((r,g,b,avg))

sort = sorted(bright, key=sorter)

for pixel in sort:
    a = list(pixel)
    a.pop()
    final.append(tuple(a))

newimg = Image.new(img.mode, img.size)
newimg.putdata(final)
newimg.save('output.png')
