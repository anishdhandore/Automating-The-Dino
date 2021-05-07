from functions import *

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
        
