#!/usr/bin/env python3
"""
This module contains one function
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    an asynchronous coroutine that takes in an
    integer argument (max_delay, with a default
    value of 10) named wait_random that waits for
    a random delay between 0 and max_delay (included
    and float value) seconds and eventually returns it.
    """
    a = random.uniform(0, (max_delay + 1))
    await asyncio.sleep(a)
    return a
