def macierz_odwrotna_gauss(macierz: list[list]) -> list[list]:
    if not macierz or type(macierz) != list or type(macierz[0]) != list:
        raise ValueError('Podana lista nie jest macierzą.')

    dim_x, dim_y = len(macierz), len(macierz[0])

    if dim_x != dim_y:
        raise ValueError('Macierz nie jest kwadratowa.')

    if dim_x != 3 or dim_y != 3:
        raise ValueError('Macierz nie jest 3x3')

    macierz_jednostkowa = []
    for i in range(0, dim_x):
        wiersz = []
        for j in range(0, dim_x):
            wiersz.append(0) if i!=j else wiersz.append(1)
        macierz_jednostkowa.append(wiersz)


    # wiersz 1
    dzielnik = macierz[0][0]
    for i in range(0, 1):
        for j in range(0, dim_x):
            macierz[i][j] = macierz[i][j] / dzielnik
            macierz_jednostkowa[i][j] = macierz_jednostkowa[i][j] / dzielnik

        # odejmujemy od wiersza 2
        mnoznik = macierz[i+1][0]
        for j in range(0, dim_x):
            macierz[i+1][j] = macierz[i+1][j] - (macierz[i][j] * mnoznik)
            macierz_jednostkowa[i+1][j] = macierz_jednostkowa[i+1][j] - (macierz_jednostkowa[i][j] * mnoznik)

        # odejmujemy od wiersza 3
        mnoznik = macierz[i+2][0]
        for j in range(0, dim_x):
            macierz[i+2][j] = macierz[i+2][j] - (macierz[i][j] * mnoznik)
            macierz_jednostkowa[i+2][j] = macierz_jednostkowa[i+2][j] - (macierz_jednostkowa[i][j] * mnoznik)

    # wiersz 2
    dzielnik = macierz[1][1]
    for i in range(1, 2):
        for j in range(0, dim_x):
            macierz[i][j] = macierz[i][j] / dzielnik
            macierz_jednostkowa[i][j] = macierz_jednostkowa[i][j] / dzielnik

        # odejmujemy od wiersza 1
        mnoznik = macierz[0][1]
        for j in range(dim_x):
            macierz[0][j] = macierz[0][j] - (macierz[i][j] * mnoznik)
            macierz_jednostkowa[0][j] = macierz_jednostkowa[0][j] - (macierz_jednostkowa[i][j] * mnoznik)

        # odejmujemy od wiersza 3
        mnoznik = macierz[2][1]
        for j in range(dim_x):
            macierz[2][j] = macierz[2][j] - (macierz[i][j] * mnoznik)
            macierz_jednostkowa[2][j] = macierz_jednostkowa[2][j] - (macierz_jednostkowa[i][j] * mnoznik)

    # wiersz 3
    dzielnik = macierz[2][2]
    for i in range(2, 3):
        for j in range(0, dim_x):
            macierz[i][j] = macierz[i][j] / dzielnik
            macierz_jednostkowa[i][j] = macierz_jednostkowa[i][j] / dzielnik

        # odejmujemy od wiersza 1
        mnoznik = macierz[0][2]
        for j in range(dim_x):
            macierz[0][j] = macierz[0][j] - (macierz[i][j] * mnoznik)
            macierz_jednostkowa[0][j] = macierz_jednostkowa[0][j] - (macierz_jednostkowa[i][j] * mnoznik)

        # odejmujemy od wiersza 2
        mnoznik = macierz[1][2]
        for j in range(dim_x):
            macierz[1][j] = macierz[1][j] - (macierz[i][j] * mnoznik)
            macierz_jednostkowa[1][j] = macierz_jednostkowa[1][j] - (macierz_jednostkowa[i][j] * mnoznik)

    # zaokraglanie do 4 miejsc po przecinku
    for x in range(dim_x):
        for y in range(dim_x):
            macierz_jednostkowa[x][y] = round(macierz_jednostkowa[x][y], 4)

    return macierz_jednostkowa


result = macierz_odwrotna_gauss([[9, 11, 6],[2, 3, 8],[12, 10, 13]])
[print(a) for a in result]

print('\n')

result = macierz_odwrotna_gauss([[2, 5, 7], [6, 3, 4], [5, -2, -3]])
[print(a) for a in result]