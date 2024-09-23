import numpy as np
import numpy.testing as nt
from in3110_instapy.numba_filters import numba_color2gray, numba_color2sepia
import in3110_instapy.io as io

#DONE
def test_color2gray(image, reference_gray):  
    gray_image = numba_color2gray(image)
    
    # Some general checks
    assert gray_image.shape == image.shape[:3]
    assert gray_image.dtype == np.uint8


    assert np.allclose(gray_image, reference_gray, atol=1500)


#DONE
def test_color2sepia(image, reference_sepia):
    
    sepia_image = numba_color2sepia(image)
    
    # Some general checks
    assert sepia_image.shape == image.shape
    assert sepia_image.dtype == np.uint8

    # reference with a larger tolerance (atol)
    assert np.allclose(sepia_image, reference_sepia, atol=5000)

