#!/usr/bin/env python3
"""
This module contains an asynchronous routine that executes multiple
"""

import asyncio
from typing import List
from random import uniform
from time import sleep


async def wait_random(max_delay: int) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The random delay.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*delays))


if __name__ == "__main__":
    import asyncio

    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
