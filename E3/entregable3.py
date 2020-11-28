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
    f = open(sys.argv[1])

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
        def __init__(self, ds, cajas_start):
            self.ds = ds
            self.n = len(self.ds)
            self.cajas_start = cajas_start  # se va modificando en cada iteracion

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
                pass

    initialps = PuzzlePS((), lista_cajas_start)
    return BacktrackingSolver.solve(initialps)


if __name__ == '__main__':
    datos = load_file2()

    if len(sys.argv) > 2:
        max_mov = sys.argv[2]

        mapa, pos_jugador, lista_cajas_start, lista_cajas_end = read_level(datos)
        print(mapa, pos_jugador, lista_cajas_start, lista_cajas_end)
        print(mapa)
    else:
        print("Introduce el numero maximo de movimientos ")
        pass
