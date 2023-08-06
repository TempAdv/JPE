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
    return image

def DarkenImage(image):
    size = image.size
    xs = size[0]; ys = size[1]
    for y in range(ys):
        
        for x in range(xs):

            #I - input O - output
            pixelI = image.getpixel((x,y))
            pixelO = []
            pixelO.append(int(pixelI[0]**2/255))
            pixelO.append(int(pixelI[1]**2/255))
            pixelO.append(int(pixelI[2]**2/255))
            pixelO.append(pixelI[3])
            pixelO = tuple(pixelO)
            image.putpixel((x,y), pixelO)
    return image

def LightenImage(image):
    size = image.size
    xs = size[0]; ys = size[1]
    for y in range(ys):
        
        for x in range(xs):

            #I - input O - output
            pixelI = image.getpixel((x,y))
            pixelO = []
            pixelO.append(int(pixelI[0]*(2-pixelI[0]/255)))
            pixelO.append(int(pixelI[1]*(2-pixelI[1]/255)))
            pixelO.append(int(pixelI[2]*(2-pixelI[2]/255)))
            pixelO.append(pixelI[3])
            pixelO = tuple(pixelO)
            image.putpixel((x,y), pixelO)
    return image

def BluenImage(image):
    size = image.size
    xs = size[0]; ys = size[1]
    for y in range(ys):
        
        for x in range(xs):

            #I - input O - output
            pixelI = image.getpixel((x,y))
            pixelO = []
            pixelO.append(int(pixelI[0]**2/255))
            pixelO.append(int(pixelI[1]**2/255))
            pixelO.append(int(pixelI[2]*(2-pixelI[2]/255)))
            pixelO.append(pixelI[3])
            pixelO = tuple(pixelO)
            image.putpixel((x,y), pixelO)
    return image

def GreenenImage(image):
    size = image.size
    xs = size[0]; ys = size[1]
    for y in range(ys):
        
        for x in range(xs):

            #I - input O - output
            pixelI = image.getpixel((x,y))
            pixelO = []
            pixelO.append(int(pixelI[0]**2/255))
            pixelO.append(int(pixelI[1]*(2-pixelI[1]/255)))
            pixelO.append(int(pixelI[2]**2/255))
            pixelO.append(pixelI[3])
            pixelO = tuple(pixelO)
            image.putpixel((x,y), pixelO)
    return image

def RedenImage(image):
    size = image.size
    xs = size[0]; ys = size[1]
    for y in range(ys):
        
        for x in range(xs):

            #I - input O - output
            pixelI = image.getpixel((x,y))
            pixelO = []
            pixelO.append(int(pixelI[0]*(2-pixelI[0]/255)))
            pixelO.append(int(pixelI[1]**2/255))
            pixelO.append(int(pixelI[2]**2/255))
            pixelO.append(pixelI[3])
            pixelO = tuple(pixelO)
            image.putpixel((x,y), pixelO)
    return image

#DL - down left
def DrawDL(img, x, y, color):
    x = x*8 ; y = y*8 

    img.putpixel((x  ,y+4), color)
    img.putpixel((x  ,y+5), color)
    img.putpixel((x  ,y+6), color)
    img.putpixel((x  ,y+7), color)
    img.putpixel((x+1,y+7), color)
    img.putpixel((x+2,y+7), color)
    img.putpixel((x+3,y+7), color)
    img.putpixel((x+1,y+6), color)

#DR - down right
def DrawDR(img, x, y, color):
    x = x*8 ; y = y*8 

    img.putpixel((x+7,y+4), color)
    img.putpixel((x+7,y+5), color)
    img.putpixel((x+7,y+6), color)
    img.putpixel((x+7,y+7), color)
    img.putpixel((x+6,y+7), color)
    img.putpixel((x+5,y+7), color)
    img.putpixel((x+4,y+7), color)
    img.putpixel((x+6,y+6), color)

#UL - up left
def DrawUL(img, x, y, color):
    x = x*8; y = y*8 

    img.putpixel((x  ,y+3), color)
    img.putpixel((x  ,y+2), color)
    img.putpixel((x  ,y+1), color)
    img.putpixel((x  ,y  ), color)
    img.putpixel((x+1,y  ), color)
    img.putpixel((x+2,y  ), color)
    img.putpixel((x+3,y  ), color)
    img.putpixel((x+1,y+1), color)

#UR - up right
def DrawUR(img, x, y, color):
    x = x*8; y = y*8

    img.putpixel((x+7,y+3), color)
    img.putpixel((x+7,y+2), color)
    img.putpixel((x+7,y+1), color)
    img.putpixel((x+7,y  ), color)
    img.putpixel((x+6,y  ), color)
    img.putpixel((x+5,y  ), color)
    img.putpixel((x+4,y  ), color)
    img.putpixel((x+6,y+1), color)

def SmoothPixelArt(imageI):
    
    size = imageI.size
    xs = size[0]; ys = size[1]

    imageO = imageI.resize((xs*8,ys*8), resample=Image.Resampling.NEAREST )

    for y in range(ys - 1):
        
        for x in range(xs - 1):

            #I - input O - output
            pixelI1 = imageI.getpixel(( x  , y   ))
            pixelI2 = imageI.getpixel(( x+1, y   ))
            pixelI3 = imageI.getpixel(( x  , y+1 ))
            pixelI4 = imageI.getpixel(( x+1, y+1 ))

            if pixelI1 == pixelI2 and pixelI2 == pixelI3 and pixelI3 == pixelI4:
                continue

            if pixelI1 == pixelI2 and pixelI1 != pixelI3 and pixelI1 != pixelI4:
                continue

            if pixelI1 == pixelI3 and pixelI1 != pixelI2 and pixelI1 != pixelI4:
                continue

            if pixelI4 == pixelI3 and pixelI4 != pixelI2 and pixelI1 != pixelI4:
                continue

            if pixelI4 == pixelI2 and pixelI4 != pixelI3 and pixelI1 != pixelI4:
                continue

            if pixelI1 == pixelI4 and pixelI2 == pixelI3 and pixelI1 != pixelI2:
                
                if pixelI1[3]==pixelI2[3]:

                    if pixelI1[0] + pixelI1[1] + pixelI1[2] > pixelI2[0] + pixelI2[1] + pixelI2[2]:

                        DrawDL(imageO, x+1, y  , pixelI1)
                        DrawUR(imageO, x  , y+1, pixelI1)

                    else:

                        DrawDR(imageO, x  , y  , pixelI2)
                        DrawUL(imageO, x+1, y+1, pixelI2)

                elif pixelI1[3]>pixelI2[3]:

                    DrawDL(imageO, x+1, y  , pixelI1)
                    DrawUR(imageO, x  , y+1, pixelI1)

                else:

                    DrawDR(imageO, x  , y  , pixelI2)
                    DrawUL(imageO, x+1, y+1, pixelI2)

                continue

            if pixelI1 == pixelI4 and pixelI1 != pixelI3 and pixelI1 != pixelI2:

                DrawDL(imageO, x+1, y  , pixelI1)
                DrawUR(imageO, x  , y+1, pixelI1)

                continue

            if pixelI2 == pixelI3 and pixelI2 != pixelI1 and pixelI2 != pixelI4:
                
                DrawDR(imageO, x  , y  , pixelI2)
                DrawUL(imageO, x+1, y+1, pixelI2)

                continue

            if pixelI1 == pixelI2 and pixelI1 == pixelI3 and pixelI1 != pixelI4:
                
                DrawUL(imageO, x+1, y+1, pixelI1)

                continue

            if pixelI1 == pixelI2 and pixelI1 == pixelI4 and pixelI1 != pixelI3:
                
                DrawUR(imageO, x, y+1, pixelI1)

                continue

            if pixelI1 == pixelI4 and pixelI1 == pixelI3 and pixelI1 != pixelI2:
                
                DrawDL(imageO, x+1, y, pixelI1)

                continue

            if pixelI4 == pixelI2 and pixelI4 == pixelI3 and pixelI1 != pixelI4:
                
                DrawDR(imageO, x, y, pixelI4)

                continue



    imageI = imageO.copy()
    return imageO

funs = {'Invert' :InvertImage ,
        'Darken' :DarkenImage ,
        'Lighten':LightenImage,
        'Reden'  :RedenImage  ,
        'Bluen'  :BluenImage  ,
        'Greenen':GreenenImage,
        'SmoothPixelArt':SmoothPixelArt}

print(files)

funname = input('Enter function name:')

fun = funs[funname]
for file in files:
    with Image.open(f"input/{file}") as im:
        img = fun(im)
        img.save(f"output/{file}")
