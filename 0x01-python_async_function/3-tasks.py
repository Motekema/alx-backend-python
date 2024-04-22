#!/usr/bin/env python3
"""
This module contains a function to create an asyncio.Task.
"""

import asyncio
from typing import Union
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


if __name__ == "__main__":
    import asyncio

    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
