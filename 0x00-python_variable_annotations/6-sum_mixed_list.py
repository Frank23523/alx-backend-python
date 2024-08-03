#!/usr/bin/env python3
"""6-sum_mixed_list.py"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing both integers and floats.

    Args:
    mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
    float: The sum of all numbers in the input list.
    """
    return float(sum(mxd_lst))
