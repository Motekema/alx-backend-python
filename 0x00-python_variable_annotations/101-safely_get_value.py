#!/usr/bin/env python3
"""
Module for annotating a function that safely retrieves a value
"""
from typing import Mapping, Any, Union, TypeVar

# Define a generic type variable
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)
-> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.

    Args:
        dct (Mapping): The dictionary to search for the key.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional): The default value to return

    Returns:
        Union[Any, T]: The value associated with the key in the dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
