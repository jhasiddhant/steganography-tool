# Import libraries
import sys
import numpy
from PIL import Image       # Import image from Python Imaging Library
numpy.set_printoptions(threshold=sys.maxsize)

# Function to Hide message in image
def hide(src, message, dest):
    
    # Saving the pixels of the source image as an array and store the size of array.
    img = Image.open(src, 'r')
    width, height = img.size
    array = numpy.array(list(img.getdata()))

    # Ckeck mode of the image
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    # Calculate total number of pixels
    total_pixels = array.size//n

    # Add delimiter ($!dd#@n+) at the end of secret message.
    message += "$!dd#@n+"
    # convert updated message to binary form and calculate the required pixels.
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    # Check if the total pixels available is sufficient or not.
    if req_pixels > total_pixels:
        print("ERROR: Need larger file size")       # prints on terminal 
        return("ERROR: Need larger file size")      # prints in GUI

    # Iterate pixels one by one and modify their LSB to the bits of the secret message
    else:
        index=0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1

        # Create and Save it as the destination output image
        array = array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest)
        print("Message Hidden Successfully")        # prints on terminal 
        return("Message Hidden Successfully")       # prints on GUI

