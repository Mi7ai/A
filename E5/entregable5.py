import sys


def load_file():
	data = dict()

	try:
		filas, columnas = sys.stdin.readline().split(" ")
		diamantes = sys.stdin.readline()
		for linea in sys.stdin.readlines():
			fila_diamante, col_diamante, valor_diamante = linea.split(" ")
			data[int(fila_diamante), int(col_diamante)] = int(valor_diamante)
	except IOError:
		print("File cannot be open!")
	return int(filas), int(columnas), int(diamantes), data


def load_file2():
	data = dict()

	f = open(sys.argv[1])

	try:
		filas, columnas = f.readline().split(" ")
		diamantes = f.readline()
		for linea in f.readlines():
			fila_diamante, col_diamante, valor_diamante = linea.split(" ")
			data[int(fila_diamante), int(col_diamante)] = int(valor_diamante)
	except IOError:
		print("File cannot be open!")
	return int(filas), int(columnas), int(diamantes), data


def diamante_rec(f, c, V: dict) -> int:
	"""
	:param V: matriz con valores de los diamantes o cero si la celda esta vacia
	:return: beneficio maximo
	"""

	def B(f: int, c: int) -> int:
		if not is_valid_square(f, c):
			return 0
		if (f, c) not in mem:
			mem[f, c] = max(B(f + 1, c) + V[f, c], B(f, c + 1) + V[f, c])
		if is_end_square(f, c):
			# devuelve el valor
			mem[f, c] = V[f, c]
		return mem[f, c]

	mem = {}
	return B(f, c)


# checks if the square is out of the grid
def is_valid_square(row, col) -> bool:
	"""
	:param row: fila que quiero comprobar
	:param col: columna que quiero comprobar
	:return: el estado de si la fila, columna esta o no en la matriz
	"""
	if row < M and col < N:
		return True
	return False


# checks weather the row, col is at the end
def is_end_square(row, col):
	if row == M - 1 and col == N - 1:
		return True
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
	sys.setrecursionlimit(5000)

	M, N, cantidad_diamantes, diamantes = load_file()
	grid = fill_dict()
	fila_start, columna_start = 0, 0

	print(diamante_rec(fila_start, columna_start, grid))
