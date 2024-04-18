#!/usr/bin/env python3
"""
Module for defining a type-annotated function sum_mixed_list
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and floats.

    Returns:
        float: The sum of the integers and floats in the input list.

    """
    return sum(mxd_lst)
