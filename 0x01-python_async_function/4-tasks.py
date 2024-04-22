#!/usr/bin/env python3
"""
This module contains a function to create an asyncio
"""

import asyncio
from typing import List, Union
from random import uniform


async def wait_random(max_delay: Union[int, float] = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (Union[int, float]): The maximum delay in seconds.

    Returns:
        float: The random delay.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: Union[int, float] = 10) -> asyncio.Task:
    """
    Create an asyncio.Task that runs the wait_random coroutine with the specified max_delay.

    Args:
        max_delay (Union[int, float]): The maximum delay in seconds.

    Returns:
        asyncio.Task: The asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*delays))


if __name__ == "__main__":
    import asyncio

    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
