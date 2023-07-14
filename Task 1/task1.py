import cv2
import numpy as np

# file containing first 2500 digits of pi
f = open('first2500DigitsOfPi.txt', 'r')
PI2500 = []
for i in range(2500):
    # reads each character one by one and stores it as float
    PI2500.append(float(f.read(1)))

# reading the corrupted pi image
piCorrupted = cv2.imread('pi_image.png')

# by analysis, the digits of pi are multiplied by 10 and stored in the array in row major order
# taking ono=ly one channel of the image because all channels are the same
piCorruptedNP = np.array(piCorrupted[:,:,0])

# list to store the digits of pi from pi_corrupted
piCorruptedNPList = []
for i in range(50):
    for j in range(50):
        piCorruptedNPList.append(piCorruptedNP[i][j] / 10)
piCorruptedNPList = np.array(piCorruptedNPList)

# checking for the digits that don't match
for i in range(2500):
    if PI2500[i] != piCorruptedNPList[i]:
        print(f'PI2500: {PI2500[i]}', f'piCorruptedNPList = {piCorruptedNPList[i]}', f'Index = {i}')

# the distorted digits are 0, 8, 3, 9 (but I spoke with Venkatesh who told it is 7 instead of 9) which are transformed to 0(0), 251(8), 94(3), 219(7)

# the 2*2 filter
filter2x2 = np.array([[251, 219],
                   [94, 0]], dtype=np.uint8)

# loading the picasso artwork and taking one channel out of it
artwork = cv2.imread('artwork_picasso.png')
artworkNP = np.array(artwork[:, :, 0])


def filterTraversalAND(img, template):
    '''
    :param img: the image on which the filter is applied
    :param template: the template for the image
    :return: the filtered image
    '''


    for i in range(0, 100, 2):
        for j in range(0, 100, 2):
            img[i][j] = template[0][0] & img[i][j]
            img[i][j+1] = template[0][1] & img[i][j+1]
            img[i+1][j] = template[1][0] & img[i+1][j]
            img[i+1][j+1] = template[1][1] & img[i+1][j+1]

    return img
def filterTraversalOR(img, template):
    '''
    :param img: the image on which the filter is applied
    :param template: the template for the image
    :return: the filtered image
    '''

    for i in range(0, 100, 2):
        for j in range(0, 100, 2):
            img[i][j] = template[0][0] | img[i][j]
            img[i][j+1] = template[0][1] | img[i][j+1]
            img[i+1][j] = template[1][0] | img[i+1][j]
            img[i+1][j+1] = template[1][1] | img[i+1][j+1]

    return img
def filterTraversalXOR(img, template):
    '''
    :param img: the image on which the filter is applied
    :param template: the template for the image
    :return: the filtered image
    '''

    for i in range(0, 100, 2):
        for j in range(0, 100, 2):
            img[i][j] = template[0][0] ^ img[i][j]
            img[i][j+1] = template[0][1] ^ img[i][j+1]
            img[i+1][j] = template[1][0] ^ img[i+1][j]
            img[i+1][j+1] = template[1][1] ^ img[i+1][j+1]

    return img


# on trying all three functions, XOR is the correct function
filterTraversalXOR(artworkNP, filter2x2)

# the collage is loaded into grayscale
collage = cv2.imread('collage.png', 0)
collageNP = np.array(collage
                     )

# the filtered image was saved(by writing a code for saving that image) and is loaded now
template = cv2.imread('template_rick.png', 0)
templateNP = np.array(template)
print(templateNP.shape, collageNP.shape)
def templateMatching(img, template):
    '''
    since the filter is 100*100 and the question requires us to find the top left coordinates of the template,
    the filter is translated along the image and the corresponding values subtracted, squared and added and stored
    in the top left corner

    :param img: the image on which template matching is done
    :param template: the template which runs (convoluted) through the image
    :return: an image of size img with the convoluted result of the template

    '''
    # multiplying an arbitrarily large number
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

# the co-ordinates of the matched image is 100, 100 so the password is 628

resultNP = templateMatching(collageNP, templateNP)

# now we find the index with least value
print(f'The index of template is ({int(np.argmin(resultNP)/800)},{np.argmin(resultNP)%800})')
# cv2.imshow('RESULT', resultNP)
# cv2.imshow('COLLAGE', collageNP)
# cv2.imshow('TEMPLATE', templateNP)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

















