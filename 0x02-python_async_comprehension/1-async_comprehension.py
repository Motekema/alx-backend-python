#!/usr/bin/env python3
"""
This module contains a coroutine that collects 10 random.
"""

import asyncio
from typing import List
from random import uniform


async def async_generator() -> float:
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension.

    Returns:
        List[float]: A list containing 10 random numbers.
    """
    return [i async for i in async_generator()]


if __name__ == "__main__":
    async def main():
        print(await async_comprehension())

    asyncio.run(main())
