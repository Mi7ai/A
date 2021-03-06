from bt_scheme import *
from typing import *
import functools
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

def cajasEsquina(cajas , mapa, lista_cajas_end):
    for caja in cajas:
        if caja not in lista_cajas_end:
            if mapa[caja[0] + 1][caja[1]] == '#' and mapa[caja[0]][caja[1] - 1] == '#':
                return True
            if mapa[caja[0] + 1][caja[1]] == '#' and mapa[caja[0]][caja[1] + 1] == '#':
                return True
            if mapa[caja[0] - 1][caja[1]] == '#' and mapa[caja[0]][caja[1] - 1] == '#':
                return True
            if mapa[caja[0] - 1][caja[1]] == '#' and mapa[caja[0]][caja[1] + 1] == '#':
                return True
    return False

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
            self.cajas_start = tuple(cajas_start)  # se va modificando en cada iteracion
            self.pos_j = pos_j  # se va modificando en cada iteracion

        def is_solution(self) -> bool:
            # comprueba si la lista de cajas_start es igual que la lista de cajas end
            return functools.reduce(lambda x, y: x and y, map(lambda a, b: a == b, self.cajas_start, lista_cajas_end), True)

        def get_solution(self) -> Solution:
            return self.ds

        def f(self) -> Union[int, float]:
            return self.n

        def state(self) -> State:
            return (self.cajas_start, self.pos_j)

        def successors(self) -> Iterable["PartialSolutionWithOptimization"]:
            if self.n < q and not cajasEsquina(self.cajas_start, mapa, lista_cajas_end):
                f = self.pos_j[0]
                c = self.pos_j[1]

                if 0 < f < len(mapa)-1 and 0 < c < len(mapa[0]) - 1:  # que se quede dentro del puzzle
                    # mirar si puedo mover el personaje donde quiero. UP!
                    if mapa[f - 1][c] != "#":  # UP
                        pos_j_nueva = (f - 1, c)
                        # mirar si hay caja
                        if pos_j_nueva in self.cajas_start:  # saber si tienes la pos del jugador en cajas
                            # estoy con el jugador encima de una caja que tengo que ver si puedo mover
                            # la posicion de la caja sera la posicion del jugador
                            pos_caja_nueva = (pos_j_nueva[0] - 1, pos_j_nueva[1])
                            if mapa[pos_j_nueva[0] - 1][pos_j_nueva[1]] != "#" and (pos_j_nueva[0] - 1, pos_j_nueva[1]) not in self.cajas_start:  # puedo mover caja UP?

                                # modifico posicion de la caja
                                cajas_start_copy = list(self.cajas_start[:])  # copia de cajas start
                                indice_caja = cajas_start_copy.index((pos_j_nueva[0], pos_j_nueva[1]))
                                cajas_start_copy[indice_caja] = pos_caja_nueva  # modifico la posicion de la caja
                                yield PuzzlePS(self.ds + ("U",), pos_j_nueva, cajas_start_copy)

                        else:
                            yield PuzzlePS(self.ds + ("U",), pos_j_nueva, self.cajas_start)
                    # mirar si puedo mover el personaje donde quiero. DOWN!
                    if mapa[f + 1][c] != "#":  # DOWN
                        pos_j_nueva = (f + 1, c)
                        # mirar si hay caja
                        if pos_j_nueva in self.cajas_start:  # saber si tienes la pos del jugador en cajas
                            # estoy con el jugador encima de una caja que tengo que ver si puedo mover
                            # la posicion de la caja sera la posicion del jugador
                            pos_caja_nueva = (pos_j_nueva[0] + 1, pos_j_nueva[1])
                            if mapa[pos_j_nueva[0] + 1][pos_j_nueva[1]] != "#" and (pos_j_nueva[0] + 1, pos_j_nueva[1]) not in self.cajas_start:  # puedo mover caja DOWN?

                                # modifico posicion de la caja
                                cajas_start_copy = list(self.cajas_start[:])  # copia de cajas start
                                indice_caja = cajas_start_copy.index((pos_j_nueva[0], pos_j_nueva[1]))
                                cajas_start_copy[indice_caja] = pos_caja_nueva  # modifico la posicion de la caja
                                yield PuzzlePS(self.ds + ("D",), pos_j_nueva, tuple(cajas_start_copy))
                        else:
                            yield PuzzlePS(self.ds + ("D",), pos_j_nueva, self.cajas_start)
                    # mirar si puedo mover el personaje donde quiero. RIGHT!
                    if mapa[f][c + 1] != "#":  # RIGHT
                        pos_j_nueva = (f, c + 1)
                        # mirar si hay caja
                        if pos_j_nueva in self.cajas_start:  # saber si tienes la pos del jugador en cajas
                            # estoy con el jugador encima de una caja que tengo que ver si puedo mover
                            # la posicion de la caja sera la posicion del jugador
                            pos_caja_nueva = (pos_j_nueva[0], pos_j_nueva[1] + 1)
                            if mapa[pos_j_nueva[0]][pos_j_nueva[1] + 1] != "#" and (pos_j_nueva[0], pos_j_nueva[1] + 1) not in self.cajas_start:  # puedo mover caja RIGHT?

                                # modifico posicion de la caja
                                cajas_start_copy = list(self.cajas_start[:])  # copia de cajas start
                                indice_caja = cajas_start_copy.index((pos_j_nueva[0], pos_j_nueva[1]))
                                cajas_start_copy[indice_caja] = pos_caja_nueva  # modifico la posicion de la caja
                                yield PuzzlePS(self.ds + ("R",), pos_j_nueva, cajas_start_copy)

                        else:
                            yield PuzzlePS(self.ds + ("R",), pos_j_nueva, self.cajas_start)

                    # mirar si puedo mover el personaje donde quiero. LEFT!
                    if mapa[f][c - 1] != "#":  # LEFT
                        pos_j_nueva = (f, c - 1)
                        # mirar si hay caja
                        if pos_j_nueva in self.cajas_start:  # saber si tienes la pos del jugador en cajas
                            # estoy con el jugador encima de una caja que tengo que ver si puedo mover
                            # la posicion de la caja sera la posicion del jugador
                            pos_caja_nueva = (pos_j_nueva[0], pos_j_nueva[1] - 1)
                            if mapa[pos_j_nueva[0]][pos_j_nueva[1] - 1] != "#" and (pos_j_nueva[0], pos_j_nueva[1] - 1) not in self.cajas_start:  # puedo mover caja LEFT?

                                # modifico posicion de la caja
                                cajas_start_copy = list(self.cajas_start[:])  # copia de cajas start
                                indice_caja = cajas_start_copy.index((pos_j_nueva[0], pos_j_nueva[1]))
                                cajas_start_copy[indice_caja] = pos_caja_nueva  # modifico la posicion de la caja
                                yield PuzzlePS(self.ds + ("L",), pos_j_nueva, cajas_start_copy)
                        else:
                            yield PuzzlePS(self.ds + ("L",), pos_j_nueva, self.cajas_start)

    initialps = PuzzlePS((), pos_jugador, lista_cajas_start)
    return BacktrackingOptSolver.solve(initialps)


if __name__ == '__main__':
    datos = load_file()

    if len(sys.argv) > 1:
        max_mov = int(sys.argv[1])
        mapa, pos_jugador, lista_cajas_start, lista_cajas_end = read_level(datos)

        solucion = list(puzzle_solve(mapa, pos_jugador, max_mov, lista_cajas_start, lista_cajas_end))

        if len(solucion) == 0:
            print("NO HAY SOLUCIÓN CON LOS MOVIMIENTOS PEDIDOS")
        else:
            print(*solucion[-1], sep="")
    else:
        print("Introduce el numero maximo de movimientos")
