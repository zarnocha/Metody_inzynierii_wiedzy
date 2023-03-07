def mnozenie_wektora(wektor: list, skalar: int):
    return list(map(lambda x: x*skalar, wektor))


wektor = [3, 0, 5]
skalar = 2

print(mnozenie_wektora(wektor=wektor, skalar=skalar))