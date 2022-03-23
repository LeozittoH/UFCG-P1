reprovados = 0
while True:
  aluno = input()
  if aluno == '-':
    break
  indice = 0
  faltas = 0
  while indice < len(aluno):
    if aluno[indice] == 'f':
      faltas += 1
    indice += 1
    if faltas > 8:
      reprovados += 1
      break
print(reprovados)