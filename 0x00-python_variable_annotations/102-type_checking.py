#!/usr/bin/env python3
"""
Module for type checking with mypy.
"""
from typing import List, Tuple


def zoom_array(lst: List, factor: int = 2) -> Tuple:
    """
    Zooms in an array by repeating each element a specified number of times.

    Args:
        lst (List): The list to zoom in.
        factor (int, optional): The factor by which to zoom in. Defaults to 2.

    Returns:
        Tuple: The zoomed-in array.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
