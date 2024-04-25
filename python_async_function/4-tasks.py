#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function task_wait_n"""

from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """The code is nearly identical to wait_n
    except task_wait_random is being called."""
    task_wait_random(max_delay)
    delay_list = []
    for i in range(n):
        delay_list.append(await wait_random(max_delay))
    return sorted(delay_list)
