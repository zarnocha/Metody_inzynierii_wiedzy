import numpy as np


def transpozycja(macierz):
    temp = np.array(macierz)
    x, y = temp.shape
    transponowana = []
    for i in range(0, y):
        kol = []
        for j in range(0, x):
            kol.append(macierz[j][i])

        transponowana.append(kol)

    return transponowana


macierz_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

macierz_2 = [
    [1, 2, 3],
    [4, 5, 6],
]

macierz_3 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print('macierz_1: ', macierz_1, '\npo transpozycji: : ', transpozycja(macierz_1), end='\n\n')
print('macierz_2: ', macierz_2, '\npo transpozycji: : ', transpozycja(macierz_2), end='\n\n')
print('macierz_3: ', macierz_3,'\npo transpozycji: : ', transpozycja(macierz_3), end='\n')
