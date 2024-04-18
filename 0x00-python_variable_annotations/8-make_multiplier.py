#!/usr/bin/env python3
"""
Module for defining a type-annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as argument and returns a functin

    Args:
        multiplier (float): The multiplier to be used in the returned function

    Returns:
        Callable[[float], float]: A function that takes a float as input.

    """
    def multiply(x: float) -> float:
        """
        Inner function that performs the multiplication.

        Args:
            x (float): The value to be multiplied.

        Returns:
            float: The result of the multiplication.

        """
        return x * multiplier

    return multiply
