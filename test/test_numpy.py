import in3110_instapy.io as io
import numpy as np
import numpy.testing as nt
from in3110_instapy.numpy_filters import numpy_color2gray, numpy_color2sepia

#DONE
def test_color2gray(image, reference_gray):
    gray_image = numpy_color2gray(image)

    assert gray_image.shape == image.shape[:3]
    assert gray_image.dtype == np.uint8

    assert np.allclose(gray_image, reference_gray, atol=5000)



#not sure how to implement this
def test_color2sepia(image, reference_sepia):

    sepia_image = numpy_color2sepia(image)

   

    
    
 

