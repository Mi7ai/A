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
    # TODO: list must contain integer not strings!!!
    try:
        nr_edificios = f.readline()
        for linea in f.readlines():
            data.append(list(linea.strip()))

    except IOError:
        print("File cannot be open!")
    return int(nr_edificios), data


class FunambulistaProblem(IDivideAndConquerProblem):
    def __init__(self, edificios: List[int]):
        self.edificios = edificios
        self.ileft = 0
        self.iright = 0

    def is_simple(self) -> "bool":
        return len(self.edificios) <= 1

    def trivial_solution(self) -> "Solution":
        return self.edificios  # not sure about this one

    def divide(self) -> "Iterable[IDivideAndConquerProblem]":
        yield FunambulistaProblem(self.edificios[:len(self.edificios) // 2])
        yield FunambulistaProblem(self.edificios[len(self.edificios) // 2:])

    def combine(self, solutions: "Iterable[Solution]") -> "Solution":
        left, right = tuple(solutions)
        i, j = 0, 0
        minv, maxv = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                minv = left[i]
                maxv = right[j]
                i += 1
                self.ileft = lista_edificios.index(minv)
                self.iright = lista_edificios.index(maxv)
            # complete with equal statement
            elif left[i] == right[j]:
                minv = left[i]
                maxv = right[j]
                self.ileft = lista_edificios.index(minv)
                self.iright = lista_edificios.index(maxv)
                i += 1
                j += 1
            else:
                maxv = left[i]
                minv = right[j]
                j += 1
        while i < len(left):
            i += 1

        while j < len(right):
            j += 1

        return (self.ileft, self.iright)


if __name__ == '__main__':
    nr_edificios, lista_edificios = load_file2()
    print(nr_edificios)
    print(lista_edificios)
    print("---")
    for lista_alturas in lista_edificios:
        problem = FunambulistaProblem(lista_alturas)
        solution = DivideAndConquerSolver().solve(problem)
        print(solution)
