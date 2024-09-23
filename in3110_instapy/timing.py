from __future__ import annotations
import sys

import time
from typing import Callable

import numpy as np
from PIL import Image

from in3110_instapy import get_filter, io


def time_one(filter_function: Callable, *arguments, calls: int = 3) -> float:
    """Return the time for one call
    When measuring, repeat the call calls times,
    and return the average.
    Args:
        filter_function (callable):
            The filter function to time
        arguments:
            Arguments to pass to filter_function
        calls (int):
            The number of times to call the function,
            for measurement
    Returns:
        time (float):
            The average time (in seconds) to run filter_function(arguments)

    """
    try:
        start_time = time.time()
        for _ in range(calls):
            filter_function(*arguments)
        end_time = time.time()
        average_time = (end_time - start_time) / calls
        #print(f"AVERAGE TIME{average_time}")
        return average_time
    except Exception as e:
        print(f"Error in time_one")
       


def make_reports(filename=str("test/rain.jpg"), calls=3):
    """
    Make timing reports for all implementations and filters
    """
    
    # Load the image
    image = np.array(Image.open(filename))
   
    # standard output to a file
    original_stdout = sys.stdout  
    with open('timing_report.txt', 'w') as f:
        sys.stdout = f  # Redirect to file
        
        # Display image name and dimensions
        print(f"\nTiming performed using {filename}: {image.shape[1]}x{image.shape[0]}")
        
        # List of filters
        filter_names = ['color2gray', 'color2sepia']
        
        # List of implementations 
        implementations = ['python', 'numpy', 'numba']  
        
        for filter_name in filter_names:
            reference_filter = get_filter(filter_name, 'python')
            reference_time = time_one(reference_filter, image, calls=calls)
            print(f"\nReference (pure Python) filter time {filter_name}: {reference_time:.10f}s (calls={calls})")
            
            for implementation in implementations:
                filter_func = get_filter(filter_name, implementation)
                filter_time = time_one(filter_func, image, calls=calls)
                speedup = reference_time / filter_time
                print(f"Timing: {implementation} {filter_name}: {filter_time:.10f}s (speedup={speedup:.2f}x)")
        
        print(f"Reference (pure Python) filter time {filter_name}: {reference_time:.10f}s (calls={calls})")
    
    #  standard output to its original state
    sys.stdout = original_stdout

if __name__ == "__main__":
    # run as `python -m in3110_instapy.timing`

    test_filter = get_filter('color2gray', 'python')
    print(f"Explicit test filter: {test_filter}")

    make_reports()
