#!/usr/bin/env python3
"""
This module contains a function to measure the runtime of wait_n coroutine.
"""

import time
from typing import Callable


async def wait_n(n: int, max_delay: int) -> float:
    """
    Asynchronous routine that spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The average time taken for each coroutine to complete.
    """
    total_time = 0
    for _ in range(n):
        start_time = time.time()
        await wait_random(max_delay)
        end_time = time.time()
        total_time += end_time - start_time
    return total_time / n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) and return total_time / n.

    Args:
        n (int): The number of times to execute wait_n.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The average time taken for each execution.
    """
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(wait_n(n, max_delay))


if __name__ == "__main__":
    import asyncio
    from random import uniform

    async def wait_random(max_delay: int) -> float:
        """
        Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.

        Args:
            max_delay (int): The maximum delay in seconds.

        Returns:
            float: The random delay.
        """
        delay = uniform(0, max_delay)
        await asyncio.sleep(delay)
        return delay

    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
