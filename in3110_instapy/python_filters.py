"""pure Python implementation of image filters"""
from __future__ import annotations

import numpy as np
from PIL import Image
import in3110_instapy.io as io

def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    height,width, _ = image.shape

    #gray_image = np.empty_like(image)
    gray_image = np.empty((height, width), dtype=np.uint8)

    # Define the weights for each color channel
    red_grey = 0.21
    green_grey = 0.72
    blue_grey = 0.07


    # iterate through the pixels, and apply the grayscale transform
    for i in range(height):  # looping through height
        for j in range(width):  # looping through width
            
            # Extract the RGB values of the pixel
            r, g, b = image[i, j]
            
            # Compute the grayscale value using the provided weights
            gray_value = r * red_grey + g * green_grey + b * blue_grey
            
            # Assign the computed grayscale value to the new image
            gray_image[i, j] = int(gray_value)

    # Convert the floating point grayscale image array to uint8
    #gray_image = gray_image.astype("uint8")

    return gray_image


def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
  
    #not used
    sepia_matrix = [
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ]

    height,width, _ = image.shape
    sepia_image = np.empty_like(image)
    # Iterate through the pixels
   
    for i in range(height):
        for j in range(width):
            r, g, b = image[i, j]
            
             # applying the sepia matrix
            new_r = int(0.393*r + 0.769*g + 0.189*b)
            new_g = int(0.349*r + 0.686*g + 0.168*b)
            new_b = int(0.272*r + 0.534*g + 0.131*b)
            
            # Clip the results to be in the valid range [0, 255]
            sepia_image[i, j] = [
                min(255, new_r),
                min(255, new_g),
                min(255, new_b)
            ]
    

    sepia_image = sepia_image.astype("uint8")

    # Return image
    return sepia_image


# #TESTING THE FUNCTIONS
# # Read the image
# image = io.read_image("/Users/ayeshaishaq/Documents/IN3110-ayeshasi/assignment3/test/rain.jpg")  # Replace with your image path

# # Apply the grayscale function
# grayscale_image = python_color2sepia(image)

# # Display the result
# io.display(grayscale_image)