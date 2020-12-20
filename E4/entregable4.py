from algoritmia.schemes.divideandconquer import IDivideAndConquerProblem, DivideAndConquerSolver
from typing import TypeVar, List 
import sys

T = TypeVar('T')


def load_file():
    data = []

    try:
        for linea in sys.stdin.readlines():
            data.append(linea)
    except IOError:
        print("File cannot be open!")
    return data


def load_file2():
    data = []
    alturas = []
    nr_edificios = 0
    f = open(sys.argv[1])

    try:
        nr_edificios = f.readline()
        for linea in f.readlines():
            for alt in linea.strip():
                data.append(int(alt))
            alturas.append(data)
            data = []

    except IOError:
        print("File cannot be open!")
    return int(nr_edificios), alturas


class FunambulistaProblem(IDivideAndConquerProblem):
    def __init__(self, edificios: List[int], b, e):
        self.edificios = edificios
        self.b = b
        self.e = e

    def is_simple(self) -> "bool":
        return len(self.edificios) <= 1

    def trivial_solution(self) -> "Solution":

        return self.edificios  # not sure about this one

    def divide(self) -> "Iterable[IDivideAndConquerProblem]":
        yield FunambulistaProblem(self.edificios[:len(self.edificios) // 2], 0, 0)
        yield FunambulistaProblem(self.edificios[len(self.edificios) // 2:], 0, 0)

    def combine(self, solutions: "Iterable[Solution]") -> "Solution":
        bestleft, bestright = tuple(solutions)  # string list numbers

        maxleft, maxright = 0, 0

        if len(bestleft) == 1:
            maxleft = bestleft[0]
            self.b = maxleft
        if len(bestright) == 1:
            maxright = bestright[0]
            self.e = maxright
        else:
            for elem in bestleft:
                if elem > maxleft:
                    maxleft = elem


            self.b = maxleft

            for elem in bestright:
                if maxleft < elem:
                    maxright = elem

            self.e = maxright


        return maxleft, maxright

    # def combine(self, solutions: "Iterable[Solution]") -> "Solution":
    #     left, right = tuple(solutions)
    #     i, j = 0, 0
    #     minv, maxv = 0, 0
    #     while i < len(left) and j < len(right):
    #         if left[i] < right[j]:
    #             minv = left[i]
    #             maxv = right[j]
    #             i += 1
    #             self.ileft = lista_edificios.index(minv)
    #             self.iright = lista_edificios.index(maxv)
    #         # complete with equal statement
    #         elif left[i] == right[j]:
    #             minv = left[i]
    #             maxv = right[j]
    #             self.ileft = lista_edificios.index(minv)
    #             self.iright = lista_edificios.index(maxv)
    #             i += 1
    #             j += 1
    #         else:
    #             maxv = left[i]
    #             minv = right[j]
    #             j += 1
    #     while i < len(left):
    #         i += 1
    #
    #     while j < len(right):
    #         j += 1
    #
    #     return (self.ileft, self.iright)


if __name__ == '__main__':
    nr_edificios, lista_edificios = load_file2()
    print(nr_edificios)
    print(lista_edificios)
    print("---")
    for lista_alturas in lista_edificios:
        problem = FunambulistaProblem(lista_alturas, 0, 0)
        solution = DivideAndConquerSolver().solve(problem)
        print(solution)
