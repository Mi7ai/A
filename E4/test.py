def slice(a):
    l1 = len(a) // 2


    print("mid1",a[:len(a) // 2])
    print("mid2",a[len(a) // 2:])

    if l1 != 0:
        slice(a[:len(a) // 2])
        print("---")
        slice(a[len(a) // 2:])

if __name__ == '__main__':
    a = [3,4,5]
    slice(a)


