def first(n, it):
    start = 0
    while start != n and start != len(it):
        yield it[start]
        start += 1


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    f = first(30, numbers)
    for i in f:
        print(i)
