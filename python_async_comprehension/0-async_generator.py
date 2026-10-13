#!/usr/bin/env python3
"""Module definissant une coroutine generateur asynchrone."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Coroutine qui genere un nombre aleatoire entre 0 et 10, dix fois."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
