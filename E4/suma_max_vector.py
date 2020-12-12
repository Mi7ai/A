# given a positive and negative integer vector
# given an b index and an e index
# calculate the best sum of the numbers between those indexes
from typing import *


def suma_max(v: List[int], b: int, e: int):
    suma = 0

    def _suma_max(b, e):
        num_elem = e - b
        if num_elem == 0:
            return 0
        if num_elem == 1:
            return v[b]
        else:
            L = _suma_max(b, (e + b) // 2)
            R = _suma_max((e + b) // 2, e)
            suma = L + R
        return suma

    return _suma_max(b, e)


def s(v, b, e):
    if b == e:
        return v[b]

    mid = (b + e) // 2

    L = s(v, b, mid) + s(v, mid, e)
    R = s(v, mid, e)

    return max(L, R)


if __name__ == '__main__':
    v = [-1, 3, 4, -5, 9, -2]
    b = 0
    e = len(v)
    print(suma_max(v, b, e))
