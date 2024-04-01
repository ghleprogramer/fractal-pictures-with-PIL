# project fractal picture with pil
import pf
from PIL import Image

imageX = 1920 # Can be any resulotion
imageY = 1080 
InsideColor = (0, 0, 0)
Xrange = (-2, .5) # mandelbrot (-2, 0.5), burning ship (-2.5, 1)
Yrange = (-1.15, 1.15) # mandelbrot (-1.15, 1.15), burning ship (-2, 1)
LoopLength = 64 # more than 100 is in not necessary
EscapeThreshold = 2 # 2 mandelbrot, 4 or 5 burning ship

# range adjustment
ratio = imageX / imageY
ValueRange = abs(Xrange[0] - Xrange[1])
adjustment = abs(ValueRange - (ValueRange * ratio)) / 2
adjustedX = (Xrange[0] - adjustment, Xrange[1] + adjustment)

image = Image.new("RGB", (imageX, imageY))
pixels = image.load()

x = pf.CreatListForRange(adjustedX, imageX)
y = pf.CreatListForRange(Yrange, imageY)
# Set, MaxEscapeVal = pf.FractalSetCreator(x, y, pf.BurningShip_loop, LoopLength, EscapeThreshold)
Set, MaxEscapeVal = pf.FractalSetCreator(x, y, pf.MandelBrot_loop, LoopLength, EscapeThreshold)

ColorRange = (0, 255)
GrayScaleList = pf.CreatListForRange(ColorRange, MaxEscapeVal + 1)

# pixel colors set to the number of iterations to escape
for i in range(imageX):
    for j in range(imageY):
        if Set[i][j] == None:
            pixels[i, j] = InsideColor
            continue
        GrayScaleColor = round(GrayScaleList[Set[i][j]])
        pixels[i, j] = (GrayScaleColor, GrayScaleColor, GrayScaleColor)

image.show()
# image.save("xxx.png", "PNG") # for png
# image.save("xxx.bmp", "BMP")
