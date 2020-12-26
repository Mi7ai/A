import sys


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
	try:
		f = open(sys.argv[1])
	except Exception:
		print("Please write the filename from where the data should be read.")

	try:
		filas, columnas = f.readline().split(" ")
		diamantes = f.readline()
		for linea in f.readlines():
			fila_diamante, col_diamante, valor_diamante = linea.split(" ")

			data.append( [int(fila_diamante), int(col_diamante), int(valor_diamante)])
	except IOError:
		print("File cannot be open!")
	return filas, columnas, data


if __name__ == '__main__':
	filas, columnas, diamantes = load_file2()
	print("{}, {}, {}".format(filas, columnas, diamantes))
