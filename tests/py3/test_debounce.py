import asyncio
from debounce import DebounceAsync
import pandas as pd
import time


def test_debounce():
    times = []

    def foo():
        times.append(time.time())

    max_wait = 50
    debounced = DebounceAsync(foo, .5 * max_wait, leading=True, max_wait=max_wait)

    async def producer(duration):
        start = time.time()
        i = 0
        while time.time() - start < duration:
            i += 1
            debounced()
            await asyncio.sleep(0)
        await asyncio.sleep(2 * debounced.max_wait)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(producer(.5))

    intervals = pd.Series(times).diff()
    assert (intervals.min() > .9 * max_wait * 1e-3)
    assert (intervals.max() < 1.1 * max_wait * 1e-3)
