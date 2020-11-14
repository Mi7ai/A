from collections.abc import Iterator, Iterable


def first(n):
    start = 0
    p = squares()
    while start != n:
        yield next(p)
        start += 1


def filter(cond, it):
    p = squares()
    for el in it:
        if cond(el):
            yield next(p)


def capicua():
    p = squares()

    while True:
        p1 = next(p)
        if is_capicua(p1):
            yield p1


def is_capicua(n):
    nr = list(str(n))
    return nr == nr[::-1]


def squares() -> Iterator[int]:
    nr = 0
    while True:
        perf = nr * nr
        nr += 1
        yield perf


if __name__ == '__main__':
    p = squares()
    print("---Cuadrados perfectos---")
    for i in first(100):
        print(i, end=" ")
    print(" ")
    print("---Cuadrados perfectos < 100--- ")
    for k in filter(lambda x: x <= 100, range(100)):
        if k < 100:
            print(k, end=" ")
    print(" ")
    print("---Primeros 20 cuadrados perfectos capicua---")
    c = capicua()
    for m in range(20):
        print(next(c), end=" ")
