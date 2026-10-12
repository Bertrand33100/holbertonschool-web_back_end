#!/usr/bin/env python3
"""Gere plusieurs coroutines asynchrones et collecte leurs resultats."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute n coroutines en concurrence et retourne les delais croissants."""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for coroutine in asyncio.as_completed(coroutines):
        delay = await coroutine
        delays.append(delay)

    return delays
