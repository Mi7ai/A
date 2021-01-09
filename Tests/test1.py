def L(q, v):
	n = len(v)
	for i in range(q // v[n - 1]):
		q = q - i * v[n - 1]
		print(i)
		n += 1


if __name__ == '__main__':
	q = 7
	v = [1, 2, 5]
	print(L(q, v))
