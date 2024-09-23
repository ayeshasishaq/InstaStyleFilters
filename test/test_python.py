from in3110_instapy.python_filters import python_color2gray, python_color2sepia

import in3110_instapy.io as io
import numpy as np

#DONE
def test_color2gray(image):
    print(f"Original Pixel: {image[0, 0]}")
    gray_image = python_color2gray(image)
    print(f"Grayscale Pixel: {gray_image[0, 0]}")
    
    # check that the result has the right shape, type
    assert gray_image.shape == image.shape[:3]  
    assert gray_image.dtype == np.uint8

    # Iterate through the pixels and compare grayscale values
    for i in range(gray_image.shape[0]):
        for j in range(gray_image.shape[1]):
            expected_gray_value = int(0.21 * image[i, j, 0] + 0.72 * image[i, j, 1] + 0.07 * image[i, j, 2])
            assert np.allclose(gray_image[i, j], expected_gray_value, atol=300)

 


#DONE
def test_color2sepia(image):
    sepia_image = python_color2sepia(image)
    
    # check that the result has the right shape, type
    assert sepia_image.shape == image.shape
    assert sepia_image.dtype == np.uint8

  # verify pixel values 
    for i in range(sepia_image.shape[0]):
        for j in range(sepia_image.shape[1]):
            r, g, b = image[i, j]
            
            new_r = 0.393*r + 0.769*g + 0.189*b
            new_g = 0.349*r + 0.686*g + 0.168*b
            new_b = 0.272*r + 0.534*g + 0.131*b
            
            # valid range [0, 255]
            expected_sepia_pixel = [
                min(255, new_r),
                min(255, new_g),
                min(255, new_b)
            ]

           
            assert np.allclose(sepia_image[i, j], expected_sepia_pixel, atol=300)