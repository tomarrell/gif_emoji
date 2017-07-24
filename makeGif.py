# Tom Arrell
# Animated Face Gif Creator

# run:
# python makeGif.py './MySquareImage.png'

import sys
from PIL import Image
import StringIO
import math as Math

# Make the initial image a square. Find the smallest size
# and crop to it to a square based on that from the top left corner.
def cropToSquare(image):
    minDimension = min(image.size)
    return image.crop((0, 0, minDimension, minDimension))

# Find the max edge width of a diamond that can fit in the square
# as it rotates.
def maxDiamondWidth(image):
    width, height = image.size
    if (width != height):
        raise Exception('Image is not square')
    return Math.floor(Math.sqrt((width / 2)**2 + (width / 2)**2))

def calcCenterOffset(image, toCenterWidth):
    imageWidth = image.size[0]
    return Math.floor((imageWidth / 2) - (toCenterWidth / 2))

def main():
    cliArgs = sys.argv
    fileName = cliArgs[1]
    imageArray = []

    im = Image.open(fileName)
    im = cropToSquare(im)

    # Calculate diamond width and offset to center crop frame
    maxWidth = maxDiamondWidth(im)
    offset = calcCenterOffset(im, maxWidth)

    for i in range(36):
        newIm = im
        newIm = newIm.rotate(10 * i, resample=Image.BICUBIC)
        cropped = newIm.crop(
            (offset, offset, maxWidth + offset, maxWidth + offset)
        ).resize((32, 32), resample=Image.BICUBIC)

        #  cropped.save('test/imageFrag_{}.png'.format(i), optimize=True)
        buff = StringIO.StringIO()
        cropped.save(buff, 'png', optimize=True)
        imageArray.append(Image.open(buff))

    # Write the image array to disc as a new GIF file
    imageArray[0].save(
        'output.gif',
        save_all=True,
        append_images=imageArray[1:],
        duration=40,
        loop=0
    )

main()
