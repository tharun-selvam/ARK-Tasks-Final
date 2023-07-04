import cv2
import numpy as np

f = open('first2500DigitsOfPi.txt', 'r')

PI2500 = []

for i in range(2500):
    PI2500.append(float(f.read(1))) #reads each character one by one and stores it as float

piCorrupted = cv2.imread('pi_image.png')

piCorruptedNP = np.array(piCorrupted[:,:,0])

#by analysis, the digits of pi are multiplied by 10 and stored in the array 51st digit on array[1][0]

piCorruptedNPList = []


for i in range(50):
    for j in range(50):
        piCorruptedNPList.append(piCorruptedNP[i][j] / 10)


piCorruptedNPList = np.array(piCorruptedNPList)
for i in range(2500):
    if PI2500[i] != piCorruptedNPList[i]:
        print(f'PI2500: {PI2500[i]}', f'piCorruptedNPList = {piCorruptedNPList[i]}', f'Index = {i}')

#the distorted digits are 0, 8, 3, 9 which are transformed to 0, 251, 94, 282

filter = np.array([[282, 251],
                   [94, 0]])
