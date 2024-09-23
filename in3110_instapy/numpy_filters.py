"""numpy implementation of image filters"""
from __future__ import annotations

import numpy as np
import in3110_instapy.io as io

def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    gray_image = np.empty_like(image)

    # weights for greyscale
    red_grey = 0.21
    green_grey = 0.72
    blue_grey = 0.07

    # Use numpy slicing 
    gray_image = (image[..., 0] * red_grey +    # all pixels from correspomding colours
                  image[..., 1] * green_grey + 
                  image[..., 2] * blue_grey)
    
    gray_image = gray_image.astype("uint8")

    # Return the grayscale image
    return gray_image


def numpy_color2sepia(image: np.array, k: float = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    (note: implementing 'k' is a bonus task,
        you may ignore it)

    Returns:
        np.array: sepia_image
    """

    if not 0 <= k <= 1:
        # validate k (optional)
        raise ValueError(f"k must be between [0-1], got {k=}")



    # define sepia matrix (optional: with stepless sepia changes)
    sepia_matrix = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])

    # HINT: For version without adaptive sepia filter, use the same matrix as in the pure python implementation
    # any way works, but you could use an Einstein sum to apply pixel transform matrix
    # or a tensor dot product, for example
    sepia_image = np.dot(image[...,:3], sepia_matrix.T)

    # Check which entries 
    np.clip(sepia_image, 0, 255, out=sepia_image)

    sepia_image = sepia_image.astype("uint8")

    # Return image (make sure it's the right type!)
    return sepia_image


# #TESTING THE FUNCTIONS
# # Read the image
# image = io.read_image("/Users/ayeshaishaq/Documents/IN3110-ayeshasi/assignment3/test/rain.jpg")  # Replace with your image path

# # Apply the grayscale function
# grayscale_image = numpy_color2sepia(image)

# # Display the result
# io.display(grayscale_image)