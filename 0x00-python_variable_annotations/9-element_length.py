#!/usr/bin/env python3
"""9-element_length.py"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    where each tuple contains a sequence from the input and its length.
    """
    return [(i, len(i)) for i in lst]
