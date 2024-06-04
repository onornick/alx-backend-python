#!/usr/bin/env python3
"""
This module contains function: 'sum_list'
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function sum_slist() takes in a list
    of float values and returns the sum in float
    """
    total = 0
    for num in input_list:
        total = total + num
    return float(total)
