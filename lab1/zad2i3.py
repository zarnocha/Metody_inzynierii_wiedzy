def dodawanie_wektorow(wektor1: list, wektor2: list):
    if len(wektor1) != len(wektor2):
        raise ValueError('Wektory nie sa rownej dlugosci.')

    return list(map(lambda x, y: x+y, wektor1, wektor2))


def iloczyn_skalarny_wektorow(wektor1: list, wektor2: list):
    if len(wektor1) != len(wektor2):
        raise ValueError('Wektory nie sa rownej dlugosci.')

    wektor = list(map(lambda x, y: x*y, wektor1, wektor2))
    return sum(wektor)


wektor1 = [3, 0, 5]
wektor2 = [6, 4, -2]

print('Suma wektorow: ', wektor1, ' + ', wektor2, ' = ', dodawanie_wektorow(wektor1=wektor1, wektor2=wektor2))
print('Iloczyn skalarny wektorow: ', wektor1, ' ∘ ', wektor2, ' = ', iloczyn_skalarny_wektorow(wektor1=wektor1, wektor2=wektor2))