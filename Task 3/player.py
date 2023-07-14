from utils import Player,WINDOW_WIDTH
import cv2
import numpy as np


def drawRectangle(img, rectangle_width, rectangle_height, location):
    cv2.rectangle(img, location, (location[0]+rectangle_width, location[1]+rectangle_height), 0, 2)


def templateMatching(img, template):
    '''
    since the filter is 100*100 and the question requires us to find the top left coordinates of the template,
    the filter is translated along the image and the corresponding values subtracted, squared and added and stored
    in the top left corner

    :param img: the image on which template matching is done
    :param template: the template which runs (convoluted) through the image
    :return: an image of size img with the convoluted result of the template

    '''

    # multiplying an arbitrarily large number to the result matrix
    resultNP = np.ones(img.shape, dtype='float64')*600000
    img_height, img_width = img.shape
    template_height, template_width = template.shape

    # resultNP = np.ones((img_height-template_height+1, img_width-template_width+1), dtype='float64')
    img.astype('float64')
    template.astype('float64')

    for i in range(0, img_height-template_height+1):
        for j in range(0, img_width-template_width+1):
            intermediate = img[i:template_height+i,j:template_width+j]
            resultNP[i][j] = np.sum((intermediate-template)**2)

    return resultNP

player = Player()
# Initializing a Player object with a random start position on a randomly generated Maze

mazeImg = player.getMap()
mazeImgNP = player.getMap()


def strategy():
    # This function is to localize the position of the newly created player with respect to the map

    localEnv = player.getSnapShot()
    localEnvNP = np.array(localEnv)
    res = templateMatching(mazeImg, localEnvNP)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    m, n = localEnvNP.shape
    drawRectangle(mazeImg, m, n, min_loc)

    # The location of the drone is the center point of the rectangle which is printed below
    print(f'The coordinates are: ({min_loc[0]+int(m/2)}, {min_loc[0]+int(n/2)})')

    return localEnvNP

if __name__ == "__main__":
    localEnvNP = strategy()


cv2.imshow('MAZE', mazeImgNP)
cv2.imshow('LOCAL', localEnvNP)
cv2.waitKey(0)
cv2.destroyAllWindows()






















