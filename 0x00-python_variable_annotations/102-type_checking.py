#!/usr/bin/env python3
"""
Module for type checking with mypy.
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in an array by repeating each element a specified number of times.

    Args:
        lst (Tuple): The list to zoom in.
        factor (int, optional): The factor by which to zoom in. Defaults to 2.

    Returns:
        List: The zoomed-in array.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
