#!/usr/bin/env python3
"""wait_n"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine that Spawns wait_random n time"""
    calls = []
    delays = []

    for i in range(n):
        call = wait_random(max_delay)
        calls.append(call)

    for call in asyncio.as_completed((calls)):
        delay = await call
        delays.append(delay)

    return delays
