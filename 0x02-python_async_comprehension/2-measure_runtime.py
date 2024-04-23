#!/usr/bin/env python3
"""
This module contains a coroutine that measures the runtime.
"""

import asyncio
from typing import List
from time import perf_counter


async def async_generator() -> float:
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield perf_counter()


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension.

    Returns:
        List[float]: A list containing 10 random numbers.
    """
    return [i async for i in async_generator()]


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing.

    Returns:
        float: The total runtime.
    """
    start_time = perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = perf_counter()
    return end_time - start_time


if __name__ == "__main__":
    async def main():
        return await measure_runtime()

    print(asyncio.run(main()))
