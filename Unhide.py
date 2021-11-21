# Import libraries
import sys
import numpy
from PIL import Image       # Import image from Python Imaging Library
numpy.set_printoptions(threshold=sys.maxsize)

# Function to Reveal message hidden in the image
def unhide(src):

    # Saving the pixels of the source image as an array
    img = Image.open(src, 'r')
    array = numpy.array(list(img.getdata()))
    
    # Ckeck mode of the image
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    # Calculating total pixels
    total_pixels = array.size//n

    # Extract the LSB from each of the pixels
    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    # Store the pixels in 8 groups starting from top-left of the image
    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    # Convert groups into ASCII characters 
    message = ""
    for i in range(len(hidden_bits)):
        if message[-8:] == "$!dd#@n+":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    
    # Check if the delimiter was found or not
    if "$!dd#@n+" in message:
        print("Hidden Message:", message[:-8])      # Display secret Message on terminal
        return (message[:-8])                       # Display secret Message on GUI
    else:
        print("No Hidden Message Found")        # Prints on terminal
        return('No Hidden Message Found')       # Prints on GUI
