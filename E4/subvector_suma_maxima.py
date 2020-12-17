from typing import *


def subvector_suma_maxima(a: List[int]) -> Tuple[int, int, int]:
    def rec(b: int, e: int) -> Tuple[int, int, int]:  # suma,b,e
        num_elem = e - b
        if num_elem == 0:  # is_simple
            return (0, 0, 0)  # trivial_solution
        if num_elem == 1:  # is_simple
            return (a[b], b, e)  # trivial_solution

        else:  # divide
            h = (b + e) // 2
            mejor_izq = rec(b, h)
            mejor_der = rec(h, e)

            suma_acum = 0
            ind_b = h
            ind_e = h
            max_sum = 0

            for i in range(h - 1, b - 1, -1):
                suma_acum += a[i]
                if suma_acum > max_sum:
                    ind_b = i
                    max_sum = suma_acum

            suma_acum = max_sum

            for i in range(h, e):
                suma_acum += a[i]
                if suma_acum > max_sum:
                    ind_e = i
                    max_sum = suma_acum

            mejor_centro = (max_sum, ind_b, ind_e)

            return max(mejor_izq, mejor_der, mejor_centro)

    return rec(0, len(a))


if __name__ == '__main__':
    # v = [-10, 6, 4, -2, 2, 8, -9, 5, -4]
    v = [-1, 3, 4, -5, 9, -2]
    print(subvector_suma_maxima(v))
