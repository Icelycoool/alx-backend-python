#!/usr/bin/env python3
"""wait_random"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that that waits for a random delay between
    0 and max_delay (inclusive) secionds.

    Args:
        max_delay (int): The maximum value for the delay. Defaults to 10.

    Returns:
        delay (float): The actual delay value.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
