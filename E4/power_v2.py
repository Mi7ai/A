def power(a, b):
    if b == 1:
        return a
    else:
        pow = power(a, b // 2) * power(a, b // 2)
    return pow
if __name__ == '__main__':
    print(power(2, 2))
