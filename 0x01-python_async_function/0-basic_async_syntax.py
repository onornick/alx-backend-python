#!/usr/bin/env python3
import random
import asyncio
async def wait_random(max_delay: int = 10) -> float:
    a = random.uniform(0, (max_delay + 1))
    await asyncio.sleep(a)
    return a


print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

   
