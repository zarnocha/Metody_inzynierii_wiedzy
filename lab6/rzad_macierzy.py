import copy
import numpy as np


def rzad_macierzy(macierz: list) -> int:
    if not macierz or not isinstance(macierz, list) or not isinstance(macierz[0], list):
        raise ValueError('Podany argument nie jest macierzą.')

    dim_x, dim_y = len(macierz), len(macierz[0])

    rzad = copy.deepcopy(dim_x)

    for i in range(0, dim_y):
        for j in range(0, dim_x):
            if i == j:
                if macierz[i][j] != 0:
                    liczba = macierz[i][j]
                else:
                    liczba = 1

                for x in range(0, dim_y):
                    macierz[i][x] = macierz[i][x] / liczba

                for k in range(0, dim_x):
                    mnoznik = copy.deepcopy(macierz[k][j])
                    for l in range(0, dim_y):
                        if k != i:
                            macierz[k][l] = macierz[k][l] - \
                                (mnoznik * macierz[i][l])

    # return macierz  # aby sprawdzic macierz końcową

    for i in range(0, dim_x):
        wiersz = np.array(macierz[i])
        if not wiersz.any():
            rzad -= 1

    return rzad


# macierz 1)

macierz_1 = [[2],
             [4],
             [6],
             [9]]

result_1 = rzad_macierzy(macierz_1)
print('Rząd macierz_1:', np.array(result_1), '\n')

# macierz 2)

macierz_2 = [[1, 2],
             [2, 4],
             [3, 6]]

result_2 = rzad_macierzy(macierz_2)
print('Rząd macierz_2:', np.array(result_2), '\n')

# macierz 3)

macierz_3 = [[1, 2, 3, 4],
             [2, 4, 6, 8]]

result_3 = rzad_macierzy(macierz_3)
print('Rząd macierz_3:', np.array(result_3), '\n')

# macierz 4)

macierz_4 = [[1, 10, 100],
             [2, 21, 200],
             [3, 30, 303],
             [4, 40, 400]]

result_4 = rzad_macierzy(macierz_4)
print('Rząd macierz_4:', np.array(result_4), '\n')

# macierz 5)

macierz_5 = [
    [1, 0, 0],
    [0, 1, 0],
    [7, 12, 0],
    [0, 6, 0],
    [6, 0, 0],
]

result_5 = rzad_macierzy(macierz_5)
print('Rząd macierz_5:', np.array(result_5), '\n')
