import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return 

# run when the screen is white
def CollisionWhiteScreen(data):
     # collision with the birds
    for i in range(550,650):
        for j in range(500,563):
            # if value of color less than 100 then consider it black!
            if (data[i,j]) < 100: 
                hit("down")
                time.sleep(0.5)
                pyautogui.keyUp("down")
                return
 
    # collision with the cactus
    for i in range(550,650):
        for j in range(563,650):
            # if value of color less than 100 then consider it black!
            if (data[i,j]) < 100:  
                hit("up")
                return
    return

# run when the screen turns dim
def CollisionBlackScreen(data):
    # collision with the birds
    for i in range(550,650):
        for j in range(500,563):
            # if value of color greater than 100 then consider it white!
            if (data[i,j]) > 100:  
                hit("down")
                time.sleep(0.5)
                pyautogui.keyUp("down")
                return
 
    # collision with the cactus
    for i in range(550,650):
        for j in range(563,650):
            # if value of color greater than 100 then consider it white!
            if (data[i,j]) > 100:  
                hit("up")
                return
    return

def CheckScreenColor(data):
    for i in range(700,900):
        for j in range(150,300):
            if data[i,j] < 100:
                # return true if screen is black/dim
                return True
    return False
        

if __name__ == '__main__':
    print("Your Dino Bot Is About To Break The Game, Are You Ready?")
    print("Start the game at chrome://dino/")
    
    time.sleep(2)

    while True:
        image = ImageGrab.grab().convert('L')  # grey images help us distinguish between colors effectively
        data = image.load()

        if CheckScreenColor(data):
            CollisionBlackScreen(data)
        else:
            CollisionWhiteScreen(data)
        
