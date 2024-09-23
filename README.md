# in3110_instapy

## Summary
in3110_instapy is a Python package made for users to run image processing. This is done with the purpose
of appliging different filters on the image. The various filters are grayscale and sepia through
implementation methods like Python, Numpy and Numba. This pacakage consist of an interface for 
image manipulation to edit photos for own desired needs.


## Installation
Python 3.8 or above needs to be installed on the system to run this code. 

Likewise, cloning the package to your repository on the local machine is required. Thereby, a virtual environment is needed to navigate within the repository, while installing the dependencies evident for the package

You can install this package using pip:
    python3 -m pip install . in the code directory

Whenever a module is needed from the package imports has been added:
    from in3110_instapy import {...}

## Usage of Cli
Using command line interface (Cli) is ran to apply filters to the image. 
The command line used is as follows:

    python -m in3110_instapy "<path-to-image>" --<filter> -o "<output-path>"
    e.g: python -m in3110_instapy "/path/to/image.jpg" --sepia -o "/path/to/output_image.jpg"

## Running other files
Also to run "timing.py" this command was used:
    python3 -m in3110_instapy.timing

To test the unit tets pytest was applied to test the functions:
    pytest test_python.py

## Applied changed in the precode
Minor modifications are applied in the __init__.py -file. That was done to proficiently test
and run the program# InstaStyleFilters
