import sys

from algoritmia.schemes.divideandconquer import IDivideAndConquerProblem
from typing import TypeVar, List

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
    nr_edificios = 0
    f = open(sys.argv[1])

    try:
        nr_edificios = f.readline()
        for linea in f.readlines():
            data.append(int(linea))
    except IOError:
        print("File cannot be open!")
    return int(nr_edificios), data


class FunambulistaProblem(IDivideAndConquerProblem):
    def __init__(self, edificios: List[T]):
        self.edificios = edificios

    def is_simple(self) -> "bool":
        return len(self.edificios) <= 1

    def trivial_solution(self) -> "Solution":
        pass

    def divide(self) -> "Iterable<IDivideAndConquerProblem>":
        pass

    def combine(self, solutions: "Iterable<Solution>") -> "Solution":
        pass


if __name__ == '__main__':
    nr_edificios, lista_edificios = load_file2()
    print(nr_edificios)
    print(lista_edificios)
    problem = FunambulistaProblem(lista_edificios)
