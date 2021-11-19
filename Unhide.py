import sys
import numpy
from PIL import Image
numpy.set_printoptions(threshold=sys.maxsize)


def unhide(src):

    img = Image.open(src, 'r')
    array = numpy.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-8:] == "$!dd#@n+":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "$!dd#@n+" in message:
        print("Hidden Message:", message[:-8])
        return (message[:-8])
    else:
        print("No Hidden Message Found")
        return('No Hidden Message Found')
