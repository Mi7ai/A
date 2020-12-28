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
	return filas, columnas, int(diamantes), data


def diamante_rec(N: int, C: int, V: List[List[int]]) -> int:
	"""
	:param N: cantidad diamantes
	:param C: suma valores diamantes
	:return: beneficio maximo
	"""

	def B(n: int, c: int) -> int:
		# --------------------
		if n == 0:
			return 0
		if (n, c) not in mem:
			if V[n - 1][2] <= c:
				mem[n, c] = max(B(n - 1, c - d * V[n - 1][2]) + d * V[n - 1][2] for d in range(2))
		return mem[n, c]
	# --------------------
	mem = {}
	return B(N, C)


if __name__ == '__main__':
	values = [90, 75, 60, 20, 10]
	weights = [4, 3, 3, 2, 2]
	capacity = 3

	# print("Versión recursiva:")
	# print(diamante_rec(values, weights, capacity))
	filas, columnas, cantidad_diamantes, diamantes = load_file2()
	suma_diamantes = 0

	for f, c, valor in diamantes:
		suma_diamantes += valor
	print(diamante_rec(cantidad_diamantes, suma_diamantes, diamantes))
# print("{}, {}, {}".format(filas, columnas, diamantes))
