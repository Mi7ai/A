import sys
from typing import *


def load_file():
	data = []
	nr_edificios = 0
	try:
		nr_edificios = sys.stdin.readline()
		for linea in sys.stdin.readlines():
			data.append(int(linea))
	except IOError:
		print("File cannot be open!")
	return nr_edificios, data


def load_file2():
	data = []
	nr_edificios = 0

	f = open(sys.argv[1])


	try:
		filas, columnas = f.readline().split(" ")
		diamantes = f.readline()
		for linea in f.readlines():
			fila_diamante, col_diamante, valor_diamante = linea.split(" ")

			data.append([int(fila_diamante), int(col_diamante), int(valor_diamante)])
	except IOError:
		print("File cannot be open!")
	return filas, columnas, data


def diamante_rec(v: List[int], w: List[int], C: int) -> int:
	def B(n: int, c: int) -> int:
		# --------------------
		if n == 0:
			return 0
		if w[n - 1] <= c:  # si el peso del objeto <= capacidad mochila
			# miro el objeto anterior con la misma capacidad
			# miro el objeto anterior con con ca capacidad - el peso del objeto + el valor del objeto
			return max(B(n - 1, c), B(n - 1, c - w[n - 1]) + v[n - 1])
		# si no cabe, miro el objeto anterior con la misma capacidad
		return B(n - 1, c)
		# --------------------

	N = len(v)
	return B(N, C)


if __name__ == '__main__':
	values = [90, 75, 60, 20, 10]
	weights = [4, 3, 3, 2, 2]
	capacity = 3

	print("Versión recursiva:")
	print(diamante_rec(values, weights, capacity))
	filas, columnas, diamantes = load_file2()
	# print("{}, {}, {}".format(filas, columnas, diamantes))
