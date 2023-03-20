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


def macierz_odwrotna(macierz: list[list]):
    det = wyznacznik(macierz=macierz)
    if det == 0:
        raise ValueError("Nie można wyznaczyć macierzy odwrotnej")

    dim_x, dim_y = len(macierz), len(macierz[0])
    if dim_x != dim_y:
        raise ValueError("Nie można wyznaczyć macierzy odwrotnej dla niekwadratowych macierzy")

    odwrotna_macierz = []

    odwrotna_macierz.append([
                            round((macierz[1][1]*macierz[2][2] - macierz[1][2]*macierz[2][1]) * (1/det), 2),
                            round((macierz[0][2]*macierz[2][1] - macierz[0][1]*macierz[2][2]) * (1/det), 2),
                            round((macierz[0][1]*macierz[1][2] - macierz[0][2]*macierz[1][1]) * (1/det), 2)
                           ])

    odwrotna_macierz.append([
                            round((macierz[1][2]*macierz[2][0] - macierz[1][0]*macierz[2][2]) * (1/det), 2),
                            round((macierz[0][0]*macierz[2][2] - macierz[0][2]*macierz[2][0]) * (1/det), 2),
                            round((macierz[0][2]*macierz[1][0] - macierz[0][0]*macierz[1][2]) * (1/det), 2)
                           ])


    odwrotna_macierz.append([
                            round((macierz[1][0]*macierz[2][1] - macierz[1][1]*macierz[2][0]) * (1/det), 2),
                            round((macierz[0][1]*macierz[2][0] - macierz[0][0]*macierz[2][1]) * (1/det), 2),
                            round((macierz[0][0]*macierz[1][1] - macierz[0][1]*macierz[1][0]) * (1/det), 2)
                           ])

    return odwrotna_macierz


macierz1 = [
    [1, 2, 3],
    [4, 5, 0],
    [7, 8, 9]
]

macierz2 = [
    [2, 5, 7],
    [6, 3, 4],
    [5, -2 , -3]
]


print('\n')

for wiersz in macierz_odwrotna(macierz=macierz1):
    print(wiersz, end='\n')

print('\n', '-'*25, '\n')

for wiersz in macierz_odwrotna(macierz=macierz2):
    print(wiersz, end='\n')

print('\n')
