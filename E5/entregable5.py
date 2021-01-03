import sys
from typing import *


# TODO: edit for this exercise
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
	data = dict()

	f = open(sys.argv[1])

	try:
		filas, columnas = f.readline().split(" ")
		diamantes = f.readline()
		for linea in f.readlines():
			fila_diamante, col_diamante, valor_diamante = linea.split(" ")
			# data.append([int(fila_diamante), int(col_diamante), int(valor_diamante)])
			data[int(fila_diamante), int(col_diamante)] = int(valor_diamante)
	except IOError:
		print("File cannot be open!")
	return int(filas), int(columnas), int(diamantes), data


def diamante_rec2(f, c, V: dict) -> int:
	"""
	:param M: filas matriz
	:param N: columnas matriz
	:param V: matriz con valores de los diamantes o cero si la celda esta vacia
	:return: beneficio maximo
	"""

	def B(f: int, c: int) -> int:
		# --------------------

		if not is_valid_square(f, c):
			return 0
		if is_valid_square(f, c):
			return V[f, c] + max(B(f + 1, c), B(f, c + 1))
		if is_end_square(f, c):
			# devuelve el valor
			valor = V[f, c]
			return valor

	# --------------------
	mem = {}
	suma_diamantes = 0
	a = 0
	return B(f, c)


# checks if the square is out of the grid
def is_valid_square(row, col) -> bool:
	"""
	:param row: fila que quiero comprobar
	:param col: columna que quiero comprobar
	:param M: filas matriz
	:param N: columnas matriz
	:return:
	"""
	if row < M and col < N:
		return True
	return False


# checks weather the row, col is at the end
def is_end_square(row, col):
	if row == M - 1 and col == N - 1: return True
	return False


# creates a dictionary in which the empty cells have value -1
def fill_dict():
	grid = dict()
	for f in range(M):
		for c in range(N):
			if (f, c) not in diamantes:
				grid[f, c] = 0
			else:
				grid[f, c] = diamantes.get((f, c))
	return grid


if __name__ == '__main__':
	M, N, cantidad_diamantes, diamantes = load_file2()

	grid = fill_dict()
	# print(grid)
	print(diamante_rec2(0, 0, grid))
	# print(diamante_iter(cantidad_diamantes, suma_diamantes, diamantes))
	# print("{}, {}, {}".format(filas, columnas, diamantes))
