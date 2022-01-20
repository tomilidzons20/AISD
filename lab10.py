from array import array
from ctypes import Array
from typing import Tuple


def binary_search(numbers: Array, value: int) -> Tuple[bool, int]:
    pp = 0
    kp = len(numbers) - 1
    while pp <= kp:
        middle = (pp + kp)//2
        if numbers[middle] == value:
            return True, middle
        if numbers[middle] < value:
            pp += 1
        if numbers[middle] > value:
            kp -= 1
    return False, -1


ints = array('I', [1, 5, 6, 7, 10, 26, 29, 40])
result = binary_search(ints, 7)
print(result)
