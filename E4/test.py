def slice(a):
	l1 = len(a) // 2

	print("indice 0 -", len(a) // 2)
	print("mid1", a[:len(a) // 2])
	print("***")
	print("indice ", len(a) // 2, "", len(a))
	print("mid2", a[len(a) // 2:])

	if l1 != 0:
		slice(a[:len(a) // 2])
		print("---")
		slice(a[len(a) // 2:])


def indice(v, i):
	return v.index(i)


if __name__ == '__main__':
	# a = [-1, 3, 4, -5, 9, -2]
	# slice(a)
	# v = list(["3", "4", "7", "7", "4", "7"])
	# print(indice(v, "7"))
	v = [881836554, 575398923, 101071365, 392655487, 625763864]
	print(sorted(v))
	for a, b in enumerate(sorted(v)):
		print(a,b)