#!/usr/bin/env python3

def sum_list(input_list: list[float]) -> float:
    total = 0
    for num in input_list:
        total = total + num
    return float(total)
