import sys
from typing import *
import fileinput

# from bt_scheme import *
Pos = Tuple[int, int]


def load_file():
    data = []

    try:
        for linea in sys.stdin.readlines():
            print(linea)
            data.append(linea)
    except IOError:
        print("File cannot be open!")
    print(sys.stdin.read(1))
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


if __name__ == '__main__':
    datos = load_file()
    # print(TypeVar(datos))
    a, b, c, d = read_level(datos)
    print(datos)
    # print(a, b, c, d)
