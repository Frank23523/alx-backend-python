#!/usr/bin/env python3
"""8-make_multiplier.py"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by a given multiplier.
    """
    def multiplier_function(x: float) -> float:
        """Inner function"""
        return x * multiplier

    return multiplier_function
