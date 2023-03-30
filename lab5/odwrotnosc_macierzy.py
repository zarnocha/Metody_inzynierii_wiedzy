import copy
import numpy as np


def macierz_odwrotna(macierz: list[list]) -> list[list]:
    if not macierz or not isinstance(macierz, list) or not isinstance(macierz[0], list):
        raise ValueError('Podana lista nie jest macierzą.')

    dim_x, dim_y = len(macierz), len(macierz[0])

    if dim_x != dim_y:
        raise ValueError('Macierz nie jest kwadratowa.')

    macierz_jednostkowa = []
    for i in range(0, dim_x):
        wiersz = []
        for j in range(0, dim_x):
            wiersz.append(0) if i != j else wiersz.append(1)
        macierz_jednostkowa.append(wiersz)

    for i in range(0, dim_x):
        for j in range(0, dim_x):
            if i == j:
                liczba = macierz[i][j]
                for x in range(0, dim_x):
                    macierz[i][x] = macierz[i][x] / liczba
                    macierz_jednostkowa[i][x] = macierz_jednostkowa[i][x] / liczba

                for k in range(0, dim_x):
                    mnoznik = copy.deepcopy(macierz[k][j])
                    for l in range(0, dim_x):
                        if k != i:
                            macierz[k][l] = macierz[k][l] - \
                                (mnoznik * macierz[i][l])
                            macierz_jednostkowa[k][l] = macierz_jednostkowa[k][l] - (
                                mnoznik * macierz_jednostkowa[i][l])

    return macierz_jednostkowa


# macierze wzięte z: https://www.math-exercises.com/matrices/inverse-matrix
# rozwiązania:       https://www.math-exercises.com/answers-inverse-matrix

# macierz g)
macierz_g = [
    [1, 2],
    [3, 5]
]

result_g = macierz_odwrotna(macierz_g)
print('macierz g):\n', np.array(result_g), '\n')


# macierz i)
macierz_i = [
    [1, 1, 1],
    [6, 5, 4],
    [13, 10, 8]
]

result_i = macierz_odwrotna(macierz_i)
print('macierz i):\n', np.array(result_i), '\n')


# macierz s)
macierz_s = [
    [3, 2, 1, 2],
    [7, 5, 2, 5],
    [0, 0, 9, 4],
    [0, 0, 11, 5]
]

result_s = macierz_odwrotna(macierz_s)
print('macierz s):\n', np.array(result_s), '\n')


# macierz z https://www.intmath.com/matrices-determinants/inverse-matrix-gauss-jordan-elimination.php
macierz = [
    [8, 2, 3, 7, 13],
    [10, 4, 5, 11, 6],
    [9, 12, 14, 15, 16],
    [17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26]
]

result = macierz_odwrotna(macierz)
print('macierz:\n', np.array(result))
