"""Command-line (script) interface to instapy"""
from __future__ import annotations

import argparse
import sys

import in3110_instapy
import numpy as np
from PIL import Image

from . import io


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
) -> None:
    """Run the selected filter"""
    # load the image from a file
    image = io.read_image(file)

    if scale != 1:
        image = io.resize_image(image, scale)

    # Logic to determine which filter and implementation to use
    if filter == "color2gray":
        if implementation == "python":
            from .python_filters import python_color2gray as filter_func
        elif implementation == "numpy":
            from .numpy_filters import numpy_color2gray as filter_func
        elif implementation == "numba":
            from .numba_filters import numba_color2gray as filter_func
        else:
            raise ValueError(f"Unknown implementation: {implementation}")

    elif filter == "color2sepia":
        if implementation == "python":
            from .python_filters import python_color2sepia as filter_func
        elif implementation == "numpy":
            from .numpy_filters import numpy_color2sepia as filter_func
        elif implementation == "numba":
            from .numba_filters import numba_color2sepia as filter_func
        else:
            raise ValueError(f"Unknown implementation: {implementation}")

    else:
        raise ValueError(f"Unknown filter: {filter}")

    # Apply the filter
    filtered = filter_func(image)

    # display the result
    if out_file:
        io.write_image(filtered, out_file)
    else:
        io.display(filtered)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(description='Apply filters to an image.')

    # adding the expected flags
    parser.add_argument('file', help='filename')
    parser.add_argument('-o', '--out', help='The output filename')
    parser.add_argument('-gray', '--gray', action='store_true', help='Select gray filter')
    parser.add_argument('-sepia', '--sepia', action='store_true', help='Select sepia filter')
    parser.add_argument('-sc', '--scale', type=int, default=1, help='Scale factor')
    parser.add_argument('-i', '--implementation', choices=['python', 'numpy', 'numba'], default='python',
                        help='The implementation')

    args = parser.parse_args(argv)

    if args.gray:
        filter = "color2gray"
    elif args.sepia:
        filter = "color2sepia"
    else:
        raise ValueError("You must specify a filter.")

    run_filter(args.file, args.out, args.implementation, filter, args.scale)