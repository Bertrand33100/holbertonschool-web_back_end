#!/usr/bin/env python3
"""Module definissant une coroutine de comprehension asynchrone."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collecte 10 nombres aleatoires via une comprehension asynchrone."""
    return [i async for i in async_generator()]
