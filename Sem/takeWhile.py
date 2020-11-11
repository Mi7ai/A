def takeWhile(cond, it):
    for el in it:
        if cond(el):
            yield el
        else:
            break


def cond(n):
    if n:
        return True
    return False


if __name__ == '__main__':
    numbers = [2, 3, 4, 5]
    f = takeWhile(lambda x: x % 2 == 0, numbers)
    for i in f:
        print(i)
