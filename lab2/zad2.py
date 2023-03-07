def mnozenie_macierzy(macierz1, macierz2):
    if len(macierz1[0]) != len(macierz2):
        return ArithmeticError('Nie mozna wymnozyc tych dwoch macierzy. '
                               'Niezgodnosc wymiarow kolumn (macierzy 1) i wierszy (macierzy 2)')

    wynik_mnozenia = []
    for i in range(len(macierz1)):
        wiersz = []
        for j in range(len(macierz2[0])):
            wynik = 0
            for k in range(len(macierz2)):
                wynik += macierz1[i][k] * macierz2[k][j]
            wiersz.append(wynik)
        wynik_mnozenia.append(wiersz)

    return wynik_mnozenia


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

x = [
    [2, 1, 3],
    [-1, 4, 0]
]

y = [
    [1, 3, 2],
    [-2, 0, 1],
    [5, -3, 2]
]

print(mnozenie_macierzy(macierz_1, macierz_3))  # mozna wymnozyc (3, 3) z (3, 2): 3 kolumny == 3 wiersze
print(mnozenie_macierzy(x, y))  # mozna wymnozyc (2, 3) z (3, 3): 3 kolumny == 3 wiersze
print(mnozenie_macierzy(macierz_2, x))  # nie mozna wymnozyc (2, 3) z (2, 3): 3 kolumny != 2 wiersze
print(mnozenie_macierzy(macierz_3, y))  # nie mozna wymnozyc (3, 2) z (3, 3):  2 kolumny != 2 wiersze
