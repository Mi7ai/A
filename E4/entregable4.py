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
	f = open(sys.argv[1])

	try:
		nr_edificios = f.readline()
		for linea in f.readlines():
			data.append(int(linea))
	except IOError:
		print("File cannot be open!")
	return nr_edificios, data


def funambulista(lista_edificios):  # la altura, indices del primer edificio, del segundo edifico, el del valle
	def rec(b: int, e: int):  # begin y end
		num_elem = e - b
		if num_elem < 3:
			return 0, 0, 0, 0
		if num_elem == 3:
			medio = (b + e) // 2
			if lista_edificios[medio] < lista_edificios[b] and lista_edificios[medio] < lista_edificios[e - 1]:
				if lista_edificios[b] > lista_edificios[e]:
					return lista_edificios[e] - lista_edificios[medio], b, e, medio
				else:
					return lista_edificios[b] - lista_edificios[medio], b, e, medio
			else:
				return 0, 0, 0, 0
		else:
			medio = (b + e) // 2
			izq = rec(b, medio)
			der = rec(medio, e)
			edificio_alto = lista_edificios[b]
			indice_alto = b

			for i in range(b, medio):
				if lista_edificios[i] > edificio_alto:
					edificio_alto = lista_edificios[i]
					indice_alto = i

			indice_alto_der = medio
			edificio_alto_der = lista_edificios[medio]
			for i in range(medio, e):
				if lista_edificios[i] > edificio_alto_der:
					edificio_alto_der = lista_edificios[i]
					indice_alto_der = i

			if edificio_alto < edificio_alto_der:
				menor_edificio = edificio_alto
				for i in range(indice_alto + 1, indice_alto_der):
					if lista_edificios[i] >= edificio_alto:
						indice_alto_der = i
						edificio_alto_der = lista_edificios[i]
						break
			else:
				menor_edificio = edificio_alto_der
				for i in range(indice_alto + 1, indice_alto_der):
					if lista_edificios[i] >= edificio_alto_der:
						indice_alto = i
						edificio_alto = lista_edificios[i]
			indices_valle = []
			valle = indice_alto
			indices_valle.append(indice_alto)
			for i in range(indice_alto + 1, indice_alto_der):
				if lista_edificios[i] < lista_edificios[valle]:
					valle = i
					indices_valle.append(i)

			centro = menor_edificio - lista_edificios[valle], indice_alto, indice_alto_der, valle

			if izq[0] == der[0] and izq[0] > centro[0]:
				if izq[3] < der[3]:
					return izq
				else:
					return der

			if izq[0] == centro[0] and izq[0] > der[0]:
				if izq[3] < der[3]:
					return izq
				else:
					return der

			if der[0] == centro[0] and der[0] > izq[0]:
				if izq[3] < der[3]:
					return izq
				else:
					return der

			if izq[0] == der[0] == centro[0]:
				if izq[3] < centro[3]:
					if izq[3] < der[3]:
						return izq
					return der
				if centro[3] < der[3]:
					if centro[3] < izq[3]:
						return centro
					return izq
				if izq[3] < der[3]:
					if der[3] < centro[3]:
						return der
					return centro

		return max(izq, der, centro)

	return rec(0, len(lista_edificios))


if __name__ == '__main__':
	nr_edificios, lista_edificios = load_file()

	sol = funambulista(lista_edificios)
	if sol[0] == 0:
		print("NO HAY SOLUCIÓN")
	else:
		print(sol[1], sol[2], sol[3], sol[0])
