import os
from PIL import Image

for root, dirs, Tfiles in os.walk("./input"):  
    files = Tfiles

def InvertImage(image):
    size = image.size
    xs = size[0]; ys = size[1]
    for y in range(ys):
        
        for x in range(xs):

            #I - input O - output
            pixelI = image.getpixel((x,y))
            pixelO = []
            pixelO.append(255 - pixelI[0])
            pixelO.append(255 - pixelI[1])
            pixelO.append(255 - pixelI[2])
            pixelO.append(pixelI[3])
            pixelO = tuple(pixelO)
            image.putpixel((x,y), pixelO)

funs = {'Invert':InvertImage}

print(files)

funname = input('Enter function name:')

fun = funs[funname]
for file in files:
    with Image.open(f"input/{file}") as im:
        fun(im)
        im.save(f"output/{file}")
