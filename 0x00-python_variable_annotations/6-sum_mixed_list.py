#!/usr/bin/env python3

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    total = 0
    for item in mxd_lst:
        total = total + item;
    return float(total)
