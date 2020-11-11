from collections.abc import Iterator, Iterable


def first(n):
    start = 0
    p = squares()
    while start != n:
        # if cond(next(p)):
        yield next(p)
        start += 1


def filter(cond, it):
    p = squares()
    for el in it:
        if cond(el):
            yield next(p)


def takeWhile(cond, it):
    for el in it:
        if cond(el):
            yield el
        else:
            break


def cond(n):
    nr = list(str(n))
    if nr == nr[::-1]:
        return True
    return False


def squares() -> Iterator[int]:
    nr = 0
    while True:
        perf = (nr * nr) + (2 * (nr + 1)) - 1
        nr += 1
        yield perf


if __name__ == '__main__':
    p = squares()
    print("---Cuadrados perfectos---")
    for i in first(100):
        print(i, end=" ")
    print(" ")
    print("---Cuadrados perfectos < 100--- ")
    for k in filter(lambda x: x < 100, range(100)):
        if k < 100:
            print(k, end=" ")
    print(" ")
    print("---Primeros 20 cuadrados capicua---")
    for m in first(20):
        if cond(m):
            print(m, end=" ")



