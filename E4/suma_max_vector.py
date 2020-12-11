# given a positive and negative integer vector
# given an b index and an e index
# calculate the best sum of the numbers between those indexes
from typing import *


def suma_max(v: List[int], b: int, e: int):
    suma = 0
    def _suma_max(b, e):


        if (e-b)//2 == 0:
            return v[b]
        else:

            suma = _suma_max(b, (e-b)//2) + _suma_max((e-b)//2, e)
            # p1 = _suma_max(b, (e-b)//2)
            # p1 += _suma_max((e-b)//2, e)
        return suma
    return _suma_max(b, e)


if __name__ == '__main__':
    v = [1,2,3,4,5]
    b = 0
    e = 5
    print(suma_max(v,b,e))