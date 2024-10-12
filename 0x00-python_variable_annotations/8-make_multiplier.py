#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a given number by the multiplier."""
    def multiply(number: float) -> float:
        return number * multiplier
    return multiply
