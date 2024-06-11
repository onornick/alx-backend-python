#!/usr/bin/env python3
'''
Task 2's module.
'''
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    '''
    Executes async_comprehension 4 times and measures the
    total execution time.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time

async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)
