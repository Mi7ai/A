import functools
import itertools

if __name__ == '__main__':
    pos_jugador = (3, 6)
    l1 = [(1, 7), (4, 4)]
    l2 = [(1, 7), (4, 4)]

    print( functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, l1, l2), True))
