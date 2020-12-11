import sys

from algoritmia.schemes.divideandconquer import IDivideAndConquerProblem, DivideAndConquerSolver


class PowerSolver(IDivideAndConquerProblem):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def is_simple(self) -> "bool":
        return self.b == 1

    def trivial_solution(self) -> "Solution":
        return self.a

    def divide(self) -> "Iterable[IDivideAndConquerProblem]":
        yield PowerSolver(self.a, self.b // 2)
        yield PowerSolver(self.a, self.b // 2)

    def combine(self, solutions: "Iterable[Solution]") -> "Solution":
        a, b = tuple(solutions)
        pow = a * b

        return pow


if __name__ == '__main__':
    print("POWER NUMBER CALCULUS")
    a = int(input("Enter base number: "))

    b = int(input("Enter exponent number: "))
    if b % 2 != 0:
        print("ONLY EVEN EXPONENT")
        sys.exit(-1)
    problem = PowerSolver(a, b)
    solution = DivideAndConquerSolver().solve(problem)
    print("{} powered {} = {}".format(a, b, solution))
