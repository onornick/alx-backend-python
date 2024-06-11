#!/usr/bin/env python3
"""
This module contains a generator func
"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    The coroutine will loop 10 times, each time
    asynchronously wait 1 second, then yield a
    random number between 0 and 10. Use the random
    module.
    """
    loop = 0
    while (loop < 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        loop += 1
