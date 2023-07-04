from utils import Player,WINDOW_WIDTH
import cv2
import numpy as np


player = Player()
    #Initializing a Player object with a random start position on a randomly generated Maze

def strategy():
    #This function is to localize the position of the newly created player with respect to the map
    pass


if __name__ == "__main__":
    strategy()

def drawRectangle(img, verticalPixels, horizontalPixels):
    player.move_horizontal(horizontalPixels)
    player.move_vertical(verticalPixels)

    localEnv = player.getSnapShot()
    localEnvNP = np.array(localEnv)

    res = cv2.matchTemplate(mazeImg, localEnv, cv2.TM_CCOEFF_NORMED) #template matching
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    m, n = localEnvNP.shape
    cv2.rectangle(mazeImgNP, max_loc, (max_loc[0]+m, max_loc[1]+n), 0, 2)

    return localEnvNP

mazeImg = player.getMap()
mazeImgNP = player.getMap()

localEnvNP = []
localEnvNP.append(drawRectangle(mazeImgNP, 0, 0))

cv2.imshow('MAZE', mazeImgNP)
cv2.imshow('LOCAL', localEnvNP)
cv2.waitKey(0)
cv2.destroyAllWindows()






















