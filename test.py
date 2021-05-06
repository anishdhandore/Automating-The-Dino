from PIL import Image, ImageGrab
import time

time.sleep(1)
image = ImageGrab.grab().convert('L')
data = image.load()
dataBird = image.load()

for i in range(550,650):
    for j in range(500,563):
        data[i,j] = 110

for i in range(550,650):
        for j in range(563,650):
            data[i,j] = 0
        
image.show()
     