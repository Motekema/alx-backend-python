#!/usr/bin/env python3
"""
Module for annotating a function that calculates the length of elements
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of elements in an iterable object.

    Args:
        lst (Iterable[Sequence]): An iterable object containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains

    """
    return [(i, len(i)) for i in lst]
