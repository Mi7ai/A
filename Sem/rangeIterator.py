from collections.abc import Iterator, Iterable


class RangeIterator:
    def __init__(self, n):
        self.current = 0
        self.last = n

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.current == self.last:
            raise StopIteration()

        n = self.current
        self.current += 1
        return n


def my_range(n) -> Iterable[int]:
    return RangeIterator(n)


if __name__ == '__main__':
    for i in my_range(2):
        print(i)
