#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer argument
named wait_random that waits for a random delay between 0 and max_delay
seconds and eventually returns it."""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """The basics of async"""
    delay = random.randint(0, max_delay)
    await asyncio.sleep(delay)
    return delay
