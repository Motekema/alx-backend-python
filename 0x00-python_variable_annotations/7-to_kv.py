#!/usr/bin/env python3
"""
Module for defining a type-annotated function to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int or float v as arguments and returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v.

    Args:
        k (str): The string key.
        v (Union[int, float]): The value which can be either an integer.

    Returns:
        Tuple[str, float]: A tuple containing the string key

    """
    return (k, v * v)
