from copy import deepcopy


def usun_kolumne_i_wiersz(macierz: list, wiersz: int, kolumna: int) -> list:
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

    if not isinstance(wiersz, int) or not isinstance(kolumna, int):
        raise ValueError(
            '\n\nPodany wiersz/ kolumna nie jest liczbą całkowitą (int).')

    if wiersz < 0 or kolumna < 0 or wiersz > len(macierz) or kolumna > len(macierz[0]):
        raise ValueError('\n\nPodano nieprawidłowy numer wiersza/ kolumny.')

    if not macierz or not isinstance(macierz, list) or not isinstance(macierz[0], list):
        raise ValueError('\n\nPodana macierz nie jest macierzą.')

    dim_x = len(macierz)
    dim_y = len(macierz[0])

    if dim_x != dim_y:
        raise ValueError('Macierz nie jest kwadratowa.')

    macierz.pop(wiersz)
    for i in range(0, len(macierz[0])-1):
        wiersz_do_wstawienia = []
        for j in range(0, len(macierz[i])):
            if j != kolumna:
                wiersz_do_wstawienia.append(macierz[i][j])
        macierz[i] = wiersz_do_wstawienia

    return macierz


def wyznacznik(macierz: list) -> int:
    '''
    Funkcja wyznacza wyznacznik metodą Laplace'a wykreślając
    odpowiednie wiersze i pierwszą kolumnę (indeks 0).
    Do wykreślania używa funkcji usun_kolumne_i_wiersz().
    Funkcja działa rekurencyjnie, na dowolnym wymiarze kwadratowej macierzy.
    '''

    if not macierz or not isinstance(macierz, list) or not isinstance(macierz[0], list):
        raise ValueError('\n\nPodana macierz nie jest macierzą.')

    dim_x, dim_y = len(macierz), len(macierz[0])

    if dim_x != dim_y:
        raise ValueError('\n\nMacierz nie jest kwadratowa.')

    if dim_x == 1:
        return macierz[0][0]

    if dim_x == 2:
        return (macierz[0][0] * macierz[1][1]) - (macierz[0][1] * macierz[1][0])

    znak = 1
    wynik = 0
    for i in range(0, dim_x):
        kopia_macierzy = macierz.copy()
        liczba = macierz[i][0]
        kopia_macierzy = usun_kolumne_i_wiersz(kopia_macierzy, i, 0)
        wynik += liczba * znak * wyznacznik(kopia_macierzy)

        znak *= -1

    return wynik


def rozwiazywanie_rownania(macierz: list) -> list:
    '''
    Funkcja rozwiązuje układ równań o dowolnej wielkości.
    Układ musi być podany w postaci macierzy.
    Układ musi posiadać tyle równań, ile zmiennych.
    Macierz musi być kwadratowa + kolumna na wolne wyrazy (liczby po znaku równości).
    Jeżeli danej zmiennej ma w równaniu nie być: należy wpisać 0 w jej miejsce.

    Przykład:
    taki układ równań:

    { 2x + 3y = 4

    { 5x - 6y = 7

    przekazujemy jako argument dla funkcji w postaci macierzy:

    macierz_arg = [
      [2, 3, 4],
      [5, 6, 7],
    ]

    rozwiazywanie_rownania(macierz=macierz_arg)
    '''

    if not macierz or not isinstance(macierz, list) or not isinstance(macierz[0], list):
        raise ValueError('Podany argument nie jest macierzą.')

    dim_x, dim_y = len(macierz), len(macierz[0])

    if dim_x != dim_y-1:
        raise ValueError('Macierz nie jest kwadratowa.\
                        Sprawdzone dla macierzy bez kolumny z wyrazami wolnymi)')

    wyrazy_wolne = []
    for wiersz in range(dim_x):
        wyrazy_wolne.append(macierz[wiersz].pop(-1))

    wyznacznik_glowny = wyznacznik(macierz)
    wyniki_wyznacznikow = []
    macierz_oryginalna = deepcopy(macierz)

    if wyznacznik_glowny != 0:
        for kolumna in range(dim_x):
            macierz = deepcopy(macierz_oryginalna)
            for wiersz in range(dim_x):
                macierz[wiersz][kolumna] = wyrazy_wolne[wiersz]
            wyniki_wyznacznikow.append(wyznacznik(macierz)/wyznacznik_glowny)

    elif wyznacznik_glowny == 0:
        for kolumna in range(dim_x):
            macierz = deepcopy(macierz_oryginalna)
            for wiersz in range(dim_x):
                macierz[wiersz][kolumna] = wyrazy_wolne[wiersz]
            wyniki_wyznacznikow.append(wyznacznik(macierz))

        wszystkie_wyznaczniki_to_zera = all(
            v == 0 for v in wyniki_wyznacznikow)

        if wyznacznik_glowny == 0 and wszystkie_wyznaczniki_to_zera:
            return "Podany układ równań ma nieskończenie wiele rozwiązań."

        if wyznacznik_glowny == 0 and not wszystkie_wyznaczniki_to_zera:
            return "Podany układ równań jest sprzeczny."

    return wyniki_wyznacznikow


# oznaczony
A = [
    [8, 1, 2, 16],
    [5, -3, -7, -22],
    [0, -5, 7, 11],
]

A_result = rozwiazywanie_rownania(A)
print('A: ', A_result)


# oznaczony
B = [
    [1, 2, 3, 3, 4],
    [1, 2, 4, 4, 5],
    [2, 3, 7, 5, 1],
    [3, 7, 8, 7, 7]
]

B_result = rozwiazywanie_rownania(B)
print('B: ', B_result)


# sprzeczny
C = [
    [1, 1, 3],
    [1, 1, 1]
]

C_result = rozwiazywanie_rownania(C)
print('C: ', C_result)


# nieoznaczony
D = [
    [1, 2, 5],
    [1, 2, 5]
]

D_result = rozwiazywanie_rownania(D)
print('D: ', D_result)


# oznaczony
E = [
    [1, 2, 5],
    [1, 1, 3]
]

E_result = rozwiazywanie_rownania(E)
print('E: ', E_result)


# oznaczony
F = [
    [1, 2, -1, 3],
    [2, 3, -4, 1],
    [3, 5, -7, 4]
]

F_result = rozwiazywanie_rownania(F)
print('F: ', F_result)


# sprzeczny
G = [
    [1, 2, 5],
    [2, 4, 20]
]

G_result = rozwiazywanie_rownania(G)
print('G: ', G_result)


# sprzeczny
H = [
    [1, 2, 5],
    [2, 4, 20]
]

H_result = rozwiazywanie_rownania(H)
print('H: ', H_result)


# nieoznaczony
I = [
    [1, 1, 1, 1, 1, 1, 10],
    [2, 2, 2, 2, 2, 2, 20],
    [3, 3, 3, 3, 3, 3, 30],
    [4, 4, 4, 4, 4, 4, 40],
    [5, 5, 5, 5, 5, 5, 50],
    [6, 6, 6, 6, 6, 6, 60]
]

I_result = rozwiazywanie_rownania(I)
print('I: ', I_result)
