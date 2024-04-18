#!/usr/bin/env python3
"""
Module for annotating a function that safely retrieves the first element
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Safely retrieves the first element of a sequence.

    Args:
        lst (Sequence): A sequence (e.g., list, tuple, string).

    Returns:
        Union[Any, None]: The first element of the sequence if the sequence
    """
    if lst:
        return lst[0]
    else:
        return None
