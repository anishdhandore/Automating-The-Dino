from PIL import Image, ImageGrab
import time

time.sleep(1)
image = ImageGrab.grab().convert('L')
data = image.load()
dataBird = image.load()

for i in range(700,900):
    for j in range(150,300):
        data[i,j] = 255
        
image.show()
     