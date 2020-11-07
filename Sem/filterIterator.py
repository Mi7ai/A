from collections.abc import Iterator, Iterable


class FilterIterator:
    def __init__(self, numbers):
        self.start = 0
        self.end = len(numbers)
        self.current = 0
        self.numbers = numbers

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.start == self.end:
            raise StopIteration()
        self.current = self.numbers[self.start]
        self.start += 1
        return self.current


#
# def cond(n):
#     if n < 100:
#         return True
#     return False


def filter(cond, data) -> Iterable[int]:
    return FilterIterator(data)


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    numbers2 = range(50, 100)
    f = filter(lambda x: x < 30, numbers)
    for i in f:
        print(i)

    # a = filter(is_even, numbers)
    #
    # for i in a:
    #
    #     print(i)
