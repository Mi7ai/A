import functools
import itertools


class Test1():
    def a(self):
        pos_jugador = (3, 6)
        l1 = [(1, 7), (4, 4)]
        l2 = [(1, 7), (4, 4)]



        print(l1 in l2)
        return functools.reduce(lambda x, y: x and y, map(lambda a, b: a == b, l1, l2), True)


class Test2():
    def a(self):
        a = [(1, 2), (3, 4)]
        b = [(4, 5), (6, 7)]
        c = a[:]
        c[0] = (0, 0)

        print(a)
        print(c)
        print(c.index((0,0)))


if __name__ == '__main__':
    test1 = Test1()
    print(test1.a())

    # test2 = Test2()
    # test2.a()
