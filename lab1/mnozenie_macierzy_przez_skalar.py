def mnozenie_wektora(wektor: list, skalar: int) -> list:
    return list(map(lambda x: x*skalar, wektor))


def mnozenie_macierzy_przez_skalar(macierz:list, skalar: int) -> list:
    macierz_zwrotna = []

    for el in macierz:
        macierz_zwrotna.append(mnozenie_wektora(wektor=el, skalar=skalar))

    return macierz_zwrotna


macierz = [[3, 0, 5], [6, 4, -2], [9, 4, 3]]
skalar = 2

print('Mnozenie macierzy przez skalar:\n', macierz, ' ∘ ', skalar, ' = ', mnozenie_macierzy_przez_skalar(macierz=macierz, skalar=skalar))