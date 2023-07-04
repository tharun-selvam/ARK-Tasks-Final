import cv2
import numpy as np

f = open('first2500DigitsOfPi.txt', 'r')
PI2500 = []
for i in range(2500):
    PI2500.append(float(f.read(1))) #reads each character one by one and stores it as float

piCorrupted = cv2.imread('pi_image.png')
piCorruptedNP = np.array(piCorrupted[:,:,0])#by analysis, the digits of pi are multiplied by 10 and stored in the array 51st digit on array[1][0]
piCorruptedNPList = []
for i in range(50):
    for j in range(50):
        piCorruptedNPList.append(piCorruptedNP[i][j] / 10)
piCorruptedNPList = np.array(piCorruptedNPList)

for i in range(2500):
    if PI2500[i] != piCorruptedNPList[i]:
        print(f'PI2500: {PI2500[i]}', f'piCorruptedNPList = {piCorruptedNPList[i]}', f'Index = {i}')

#the distorted digits are 0, 8, 3, 9 which are transformed to 0, 251, 94, 282

filter2x2 = np.array([[282, 251],
                   [94, 0]], dtype=np.uint8)

artwork = cv2.imread('artwork_picasso.png')
artworkNP = np.array(artwork[:, :, 0])


def filterTraversalAND(img, template):
    filteredNPAND = np.zeros((100, 100))
    for i in range(0, 100, 2):
        for j in range(0, 100, 2):
            filteredNPAND[i][j] = template[0][0] & img[i][j]
            filteredNPAND[i][j+1] = template[0][1] & img[i][j+1]
            filteredNPAND[i+1][j] = template[1][0] & img[i+1][j]
            filteredNPAND[i+1][j+1] = template[1][1] & img[i+1][j+1]
    return filteredNPAND

def filterTraversalOR(img, template):
    filteredNPOR = np.zeros((100, 100))
    for i in range(0, 100, 2):
        for j in range(0, 100, 2):
            filteredNPOR[i][j] = template[0][0] | img[i][j]
            filteredNPOR[i][j+1] = template[0][1] | img[i][j+1]
            filteredNPOR[i+1][j] = template[1][0] | img[i+1][j]
            filteredNPOR[i+1][j+1] = template[1][1] | img[i+1][j+1]
    return filteredNPOR

def filterTraversalXOR(img, template):
    filteredNPXOR = np.zeros((100, 100))
    for i in range(0, 100, 2):
        for j in range(0, 100, 2):
            filteredNPXOR[i][j] = template[0][0] ^ img[i][j]
            filteredNPXOR[i][j+1] = template[0][1] ^ img[i][j+1]
            filteredNPXOR[i+1][j] = template[1][0] ^ img[i+1][j]
            filteredNPXOR[i+1][j+1] = template[1][1] ^ img[i+1][j+1]
    return filteredNPXOR


filteredNPAND = filterTraversalAND(artworkNP, filter2x2)
filteredNPOR = filterTraversalOR(artworkNP, filter2x2)
filteredNPXOR = filterTraversalXOR(artworkNP, filter2x2)

filteredSup = cv2.merge([filteredNPXOR, filteredNPOR, filteredNPAND])
print(filteredNPAND)

cv2.imshow('ORIGINAL', artworkNP)
cv2.imshow('FILTERED_AND', filterTraversalAND(artworkNP, filter2x2))
cv2.imshow('FILTERED_OR', filterTraversalOR(artworkNP, filter2x2))
cv2.imshow('FILTERED_XOR', filterTraversalXOR(artworkNP, filter2x2))
cv2.imshow('IMPOSED', filteredSup)

cv2.waitKey(0)
cv2.destroyAllWindows()
