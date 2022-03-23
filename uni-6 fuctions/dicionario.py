faltaram = 0
while True:
  frequencia = input()
  if frequencia == "-":
    break
  indice = 0
  contador = 0
  while indice < len(frequencia):
    if frequencia[indice]=="f":
      contador += 1
    indice+=1
    if contador > 8:
      faltaram+=1
      break
print(faltaram)