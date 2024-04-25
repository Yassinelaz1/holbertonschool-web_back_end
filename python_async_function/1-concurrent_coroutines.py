#!/usr/bin/env python3
""" execute multiple coroutines at the same time with async"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Return the list of delays in ascending order"""
    list = []
    for i in range(n):
        delays = await wait_random(max_delay)
        list.append(delays)
    return sorted(list)
