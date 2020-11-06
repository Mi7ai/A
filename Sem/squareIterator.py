from collections.abc import Iterator, Iterable


class SquareIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.powered = []

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> list:
        if len(self.powered) == len(self.numbers):
            raise StopIteration

        for i in self.numbers:
            self.powered.append(i * i)

        return self.powered


def square(numbers) -> Iterable[int]:
    return SquareIterator(numbers)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    for nr in square(numbers):
        print(nr)
