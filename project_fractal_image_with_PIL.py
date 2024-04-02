# project fractal picture with pil
import pf
from PIL import Image

imageX = 1920 # 720 1280 1920 # Can be any resulotion
imageY = 1080 # 480 720 1080 
InsideColor = (0, 0, 0)
Xrange = (-2, 0.5) # mandelbrot (-2, 0.5), burning ship (-2.5, 1)
Yrange = (-1.15, 1.15) # mandelbrot (-1.15, 1.15), burning ship (-2, 1)
LoopLength = 100 # fractal equation max iteration
EscapeThreshold = 2 # 2 mandelbrot, 4 or 5 burning ship

image = Image.new("RGB", (imageX, imageY))
pixels = image.load()

adjusted_X = pf.RatioAdjustor(imageX, imageY, Xrange, Yrange)
x = pf.CreatListForRange(adjusted_X, imageX)
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
# image.save("the_mandelbrot_fractal_seahorse_tail_zoom_4.png", "PNG") # for png
# image.save("the_mandelbrot_fractal_seahorse_tail_zoom_4.bmp", "BMP") # for bmp
