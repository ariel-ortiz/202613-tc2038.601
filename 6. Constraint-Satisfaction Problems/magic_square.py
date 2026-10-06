from typing import NamedTuple, cast
from csp import Constraint, CSP


type Grid = list[list[int]]


class GridLocation(NamedTuple):
    row: int
    column: int


def convert_to_grid(assignment: dict[int, GridLocation]) -> Grid:
    result: Grid = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
    for (variable, (row, column)) in assignment.items():
        result[row][column] = variable
    return result


if __name__ == '__main__':
    a: GridLocation = GridLocation(1, 2)
    print(f'{a = }')
    b: GridLocation = GridLocation(1, 2)
    print(f'{b = }')
    print(f'{(a == b) = }')
    c: GridLocation = GridLocation(2, 2)
    print(f'{c = }')
    print(f'{(a == c) = }')
    (x, y) = a
    print(f'{x = }')
    print(f'{y = }')
    print(f'{a[0] = }')
    print(f'{a[1] = }')
    print(f'{a.row = }')
    print(f'{a.column = }')
    print(convert_to_grid({
        1: GridLocation(0, 0),
        2: GridLocation(0, 1),
        3: GridLocation(0, 2),
        4: GridLocation(1, 0),
        5: GridLocation(1, 1),
        6: GridLocation(1, 2),
        7: GridLocation(2, 0),
        8: GridLocation(2, 1),
        9: GridLocation(2, 2)
    }))

