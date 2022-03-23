positivos = 0

for i in range(0,6):
    valores = input().split()
    for i in range(len(valores)):
        if valores[i] > '0':
          positivos += 1

print(f'{positivos} valores positivos')