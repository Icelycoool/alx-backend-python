#!/usr/bin/env python3
"""task_wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine that Spawns task_wait_random n time"""
    calls = []
    delays = []

    for i in range(n):
        call = task_wait_random(max_delay)
        calls.append(call)

    for call in asyncio.as_completed((calls)):
        delay = await call
        delays.append(delay)

    return delays
