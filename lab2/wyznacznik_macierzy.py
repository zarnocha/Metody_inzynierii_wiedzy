def usun_kolumne_i_wiersz(macierz: list[list], wiersz: int, kolumna: int) -> list[list]:

    '''
    Funkcja wykreśla odpowiedni wiersz i kolumnę z podanej w argumencie macierzy.
    Zwracana jest macierz bez wiersza i kolumny o podanych indeksach.\n
    Przykład:\n
    argumenty:\n
    macierz:[
                        [1,2,3],\n
                        [4,5,6],\n
                        [7,8,9]\n
                        ],
    wiersz: 0, kolumna: 0.

    Rezultat = [
        [5,6],\n
        [8,9]\n
        ]
    '''

    if type(wiersz) != int or type(kolumna) != int:
        raise ValueError('\n\nPodany wiersz/ kolumna nie jest liczbą całkowitą (int).')

    elif wiersz < 0 or kolumna < 0 or wiersz > len(macierz) or kolumna > len(macierz[0]):
        raise ValueError('\n\nPodano nieprawidłowy numer wiersza/ kolumny.')

    if not macierz or type(macierz) != list or type(macierz[0]) != list:
        raise ValueError('\n\nPodana macierz nie jest macierzą.')

    dim_x = len(macierz)
    dim_y = len(macierz[0])

    if dim_x != dim_y:
        return ValueError('Macierz nie jest kwadratowa.')

    macierz.pop(wiersz)
    for i in range(0, len(macierz[0])-1):
        wiersz = []
        for j in range(0, len(macierz[i])):
            if j != kolumna:
                wiersz.append(macierz[i][j])
        macierz[i] = wiersz

    return macierz


def wyznacznik(macierz: list[list]) -> int:

    '''
    Funkcja wyznacza wyznacznik metodą Laplace'a wykreślając odpowiednie wiersze i pierwszą kolumnę (indeks 0).
    Do wykreślania używa funkcji usun_kolumne_i_wiersz().
    Funkcja działa rekurencyjnie, na dowolnym wymiarze kwadratowej macierzy.
    '''

    if not macierz or type(macierz) != list or type(macierz[0]) != list:
        raise ValueError('\n\nPodana macierz nie jest macierzą.')

    dim_x, dim_y = len(macierz), len(macierz[0])

    if dim_x != dim_y:
        raise ValueError('\n\nMacierz nie jest kwadratowa.')

    if dim_x == 1:
        return macierz[0][0]

    if dim_x == 2:
        return (macierz[0][0] * macierz[1][1]) - (macierz[0][1] * macierz[1][0])

    else:
        znak = 1
        wynik = 0
        for i in range(0, dim_x):
            kopia_macierzy = macierz.copy()
            liczba = macierz[i][0]
            kopia_macierzy = usun_kolumne_i_wiersz(kopia_macierzy, i, 0)
            wynik += liczba * znak * wyznacznik(kopia_macierzy)

            znak *= -1

        return wynik


macierz1 = [   # wyznacznik = -2
    [1, 2],
    [3, 4],
]

macierz2 = [   # wyznacznik = -36
    [1, 2, 3],
    [4, 5, 0],
    [7, 8, 9]
]

macierz3 = [   # wyznacznik = -160
    [1, -1, 2, 4],
    [0, 1, 0, 3],
    [5, 7, -2, 0],
    [2, 0, -1, 4]
]

macierz4 = [   # wyznacznik = -24
    [0, 2, 3, 4],
    [5, 0, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

macierz5 = [   # wyznacznik = 9
    [9]
]

macierz6 = [   # wyznacznik = -33
    [1, 3, 4],
    [0, 3, 0],
    [2, -2, -3]
]

# macierz7 = [1, 2]    # błąd

# macierz8 = 'a'       # błąd

# macierz9 = 9         # błąd

# macierz10 = [[1, 5, 0, 6, 8, 7, 7, 6, 9, 8],   # wyznacznik = -114257576
#             [8, 6, 3, 1, 0, 6, 2, 3, 3, 6],
#             [3, 3, 3, 4, 4, 4, 1, 3, 4, 5],
#             [1, 5, 2, 2, 2, 2, 8, 5, 1, 1],
#             [4, 8, 8, 7, 1, 3, 3, 6, 8, 2],
#             [7, 6, 7, 1, 8, 6, 1, 2, 7, 8],
#             [7, 9, 0, 6, 8, 5, 7, 0, 1, 8],
#             [8, 9, 1, 5, 7, 8, 4, 2, 2, 5],
#             [1, 9, 4, 4, 4, 5, 4, 7, 5, 4],
#             [5, 8, 1, 3, 4, 4, 5, 7, 5, 0]
# ]

print('Wyznacznik macierz1 = ', wyznacznik(macierz1), end='\n\n')
print('Wyznacznik macierz2 = ', wyznacznik(macierz2), end='\n\n')
print('Wyznacznik macierz3 = ', wyznacznik(macierz3), end='\n\n')
print('Wyznacznik macierz4 = ', wyznacznik(macierz4), end='\n\n')
print('Wyznacznik macierz5 = ', wyznacznik(macierz5), end='\n\n')
print('Wyznacznik macierz6 = ', wyznacznik(macierz6), end='\n\n')
# print('Wyznacznik macierz7 = ', wyznacznik(macierz7), end='\n\n')
# print('Wyznacznik macierz8 = ', wyznacznik(macierz8), end='\n\n')
# print('Wyznacznik macierz9 = ', wyznacznik(macierz9), end='\n\n')
# print('Wyznacznik macierz10 = ', wyznacznik(macierz10), end='\n\n')
