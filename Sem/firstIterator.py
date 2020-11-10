from collections.abc import Iterator, Iterable


class FirstIterator:
    def __init__(self, current, rangeNumbers):
        self.start = 0
        self.end = len(rangeNumbers)
        self.current = current
        self.res = 0
        self.rangeNumbers = rangeNumbers

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.end or self.start == self.current:
            raise StopIteration

        self.res = self.rangeNumbers[self.start]
        self.start += 1

        return self.res


def first(n, numbers):
    return FirstIterator(n, numbers)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    for nr in first(2, numbers):
        print(nr)
