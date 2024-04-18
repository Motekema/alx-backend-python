#!/usr/bin/env python3
"""
Module for defining a type-annotated function sum_list
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of the input list.

    """
    return sum(input_list)
