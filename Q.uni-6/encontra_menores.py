def encontra_menores(num, lista):
    numero = -1

    for i in range(len(lista)):
        if lista[i] < num:
            numero = lista[i]
            break
        else:
            numero = -1
    return numero

lista1 = [100, 200, 300, 400]
lista2 = [15, 12, 4, 9, 10]

assert encontra_menores(100, lista1) ==  -1
assert encontra_menores(10, lista2) ==  4