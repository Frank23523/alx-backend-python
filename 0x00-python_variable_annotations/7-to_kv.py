#!/usr/bin/env python3
"""7-to_kv.py"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int or float, and returns a tuple.
    """
    return (k, float(v ** 2))
