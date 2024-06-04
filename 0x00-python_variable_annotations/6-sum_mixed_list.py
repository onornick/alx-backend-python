#!/usr/bin/env python3
"""
This module has one function: 'sum_mixed_list'
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function sum_mixed_list which takes a
    list mxd_lst of integers and floats and
    returns their sum as a float
    """
    total = 0
    for item in mxd_lst:
        total = total + item
    return float(total)
