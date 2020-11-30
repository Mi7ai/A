import functools

from bt_scheme import PartialSolution, Solution, BacktrackingSolver
from typing import *
import sys

Pos = Tuple[int, int]


def load_file():
    data = []

    try:
        for linea in sys.stdin.readlines():
            data.append(linea)
    except IOError:
        print("File cannot be open!")
    return data


def load_file2():
    data = []
    f = open(sys.argv[2])

    try:
        for linea in f.readlines():
            data.append(str(linea))
    except IOError:
        print("File cannot be open!")
    return data


def read_level(puzle_lines: List[str]) -> Tuple[List[str], Pos, List[Pos], List[Pos]]:
    # Averigua la posición del jugador y las posiciones iniciales y finales de las cajas
    player_pos, boxes_start, boxes_end = None, [], []
    num_rows = len(puzle_lines)
    num_cols = len(puzle_lines[0].strip())

    for r in range(num_rows):
        for c in range(num_cols):
            if puzle_lines[r][c] == 'p':
                player_pos = (r, c)
            elif puzle_lines[r][c] == 'o':
                boxes_start.append((r, c))
            elif puzle_lines[r][c] == 'x':
                boxes_end.append((r, c))

    # Crea un mapa (incluye únicamente paredes y pasillos, borra 'p','x' y 'o'):
    tr = str.maketrans("pxo", "   ")
    level_map = []
    for l in puzle_lines:
        level_map.append(l.strip().translate(tr))

    return level_map, player_pos, boxes_start, boxes_end


# comprobar fuera el numero de mov con la longitud de la lista
def puzzle_solve(mapa, pos_jugador, q, lista_cajas_start, lista_cajas_end):
    class PuzzlePS(PartialSolution):
        """
        Parameters:

        ds: lista de decisiones
        n = longitud lista de decisiones, por comodidad
        cajas_start: lista con las posiciones de las cajas que se van modificando donde las muevo(no se si esta bien)
        """
        def __init__(self, ds, pos_j, cajas_start):
            self.ds = ds
            self.n = len(self.ds)
            self.cajas_start = cajas_start  # se va modificando en cada iteracion
            self.pos_j = pos_j  # se va modificando en cada iteracion

        def is_solution(self) -> bool:
            # comprueba si la lista de cajas_start es igual que la lista de cajas end
            return functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, self.cajas_start, lista_cajas_end),
                                    True)

        def get_solution(self) -> Solution:
            return self.ds

        # def f(self) -> Union[int, float]:
        #     pass
        #
        # def state(self) -> State:
        #     pass

        def successors(self) -> Iterable["PartialSolution"]:
            if self.n < q:
                f = self.pos_j[0]
                c = self.pos_j[1]
                if f > 0 and c > 0:
                    # mirar si puedo mover el personaje donde quiero. UP!
                    if mapa[f - 1][c] != "#":  # UP
                        pos_j_nueva = (f - 1, c)
                        # mirar si hay caja
                        if pos_j_nueva in self.cajas_start:  # saber si tienes la pos del jugador en cajas
                            # estoy con el jugador encima de una caja que tengo que ver si puedo mover
                            # la posicion de la caja sera la posicion del jugador
                            if mapa[pos_j_nueva[0]][pos_j_nueva[1]] != "#":  # puedo mover caja UP?
                                # modifico posicion de la caja
                                cajas_start_copy = self.cajas_start[:]  # copia de cajas start
                                indice_caja = cajas_start_copy.index((pos_j_nueva[0], pos_j_nueva[1]))
                                cajas_start_copy[indice_caja] = pos_j_nueva  # modifico la posicion de la caja
                                yield PuzzlePS(self.ds + (0,), pos_j_nueva, cajas_start_copy)

                        # yield PuzzlePS(self.ds + (0,), pos_j_nueva, self.cajas_start)
                    # mirar si puedo mover el personaje donde quiero. RIGHT!
                    if mapa[f][c + 1] != "#":  # RIGHT
                        pos_j_nueva = (f, c + 1)
                        # mirar si hay caja
                        if pos_j_nueva in self.cajas_start:  # saber si tienes la pos del jugador en cajas
                            # estoy con el jugador encima de una caja que tengo que ver si puedo mover
                            # la posicion de la caja sera la posicion del jugador
                            if mapa[pos_j_nueva[0]][pos_j_nueva[1]] != "#":  # puedo mover caja RIGHT?
                                # modifico posicion de la caja
                                cajas_start_copy = self.cajas_start[:]  # copia de cajas start
                                indice_caja = cajas_start_copy.index((pos_j_nueva[0], pos_j_nueva[1]))
                                cajas_start_copy[indice_caja] = pos_j_nueva  # modifico la posicion de la caja
                                yield PuzzlePS(self.ds + (1,), pos_j_nueva, cajas_start_copy)

                        # yield PuzzlePS(self.ds + (1,), pos_j_nueva, self.cajas_start)
                    # mirar si puedo mover el personaje donde quiero. DOWN!
                    if mapa[f + 1][c] != "#":  # DOWN
                        pos_j_nueva = (f + 1, c)
                        # mirar si hay caja
                        if pos_j_nueva in self.cajas_start:  # saber si tienes la pos del jugador en cajas
                            # estoy con el jugador encima de una caja que tengo que ver si puedo mover
                            # la posicion de la caja sera la posicion del jugador
                            if mapa[pos_j_nueva[0]][pos_j_nueva[1]] != "#":  # puedo mover caja DOWN?
                                # modifico posicion de la caja
                                cajas_start_copy = self.cajas_start[:]  # copia de cajas start
                                indice_caja = cajas_start_copy.index((pos_j_nueva[0], pos_j_nueva[1]))
                                cajas_start_copy[indice_caja] = pos_j_nueva  # modifico la posicion de la caja
                                yield PuzzlePS(self.ds + (2,), pos_j_nueva, cajas_start_copy)
                        # yield PuzzlePS(self.ds + (2,), pos_j_nueva, self.cajas_start)
                    # mirar si puedo mover el personaje donde quiero. LEFT!
                    if mapa[f][c - 1] != "#":  # LEFT
                        pos_j_nueva = (f, c - 1)
                        # mirar si hay caja
                        if pos_j_nueva in self.cajas_start:  # saber si tienes la pos del jugador en cajas
                            # estoy con el jugador encima de una caja que tengo que ver si puedo mover
                            # la posicion de la caja sera la posicion del jugador
                            if mapa[pos_j_nueva[0]][pos_j_nueva[1] - 1] != "#":  # puedo mover caja LEFT?
                                pos_caja_nueva = (pos_j_nueva[0],pos_j_nueva[1] - 1)
                                # modifico posicion de la caja
                                cajas_start_copy = self.cajas_start[:]  # copia de cajas start
                                indice_caja = cajas_start_copy.index((pos_j_nueva[0], pos_j_nueva[1]))
                                cajas_start_copy[indice_caja] = pos_caja_nueva  # modifico la posicion de la caja
                                yield PuzzlePS(self.ds + (3,), pos_j_nueva, cajas_start_copy)
                        # yield PuzzlePS(self.ds + (3,), pos_j_nueva, self.cajas_start)
                    # si no encuentro ninguna caja en ninguna de las direcciones
                    # me voy a cada una de ellas, 4 lineas de yield modificando la direccion, las mismas cajas
                    # pos_j modificada para cada direccion
                    yield PuzzlePS(self.ds + (0,), (f - 1, c), self.cajas_start)  # UP
                    yield PuzzlePS(self.ds + (1,), (f, c + 1), self.cajas_start)  # RIGHT
                    yield PuzzlePS(self.ds + (2,), (f + 1, c), self.cajas_start)  # DOWN
                    yield PuzzlePS(self.ds + (3,), (f, c - 1), self.cajas_start)  # LEFT

    initialps = PuzzlePS((), pos_jugador, lista_cajas_start)
    return BacktrackingSolver.solve(initialps)


if __name__ == '__main__':
    datos = load_file2()

    if len(sys.argv) > 1:
        max_mov = int(sys.argv[1])
        mapa, pos_jugador, lista_cajas_start, lista_cajas_end = read_level(datos)

        f = pos_jugador[0]
        c = pos_jugador[1]

        for sol in puzzle_solve(mapa, pos_jugador, max_mov, lista_cajas_start, lista_cajas_end):
            print(sol)
            print("Works but no sol found")

    else:
        print("Introduce el numero maximo de movimientos ")
        pass
