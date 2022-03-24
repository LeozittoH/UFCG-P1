def meu_split(string):
   
    termo = ''
    termos_atribuidos = []    
    for i in range(len(string)): 
        if string[i] == ' ':
            termos_atribuidos.append(termo)
            termo = ''
        if i == len(string)-1:
            termo += string[i]
            termos_atribuidos.append(termo)   
        else:
            termo += string[i]
    return termos_atribuidos

maconha = meu_split('maconha é vida')
print(maconha)

def maior_idade(lista_de_nomes,lista_de_idades):
    lista_maiores = ''
    for i in range(len(lista_de_nomes)):
        if int(lista_de_idades[i]) >= 18:
            lista_maiores += lista_de_nomes[i]
    print(len(lista_maiores))
    return lista_maiores

entrada = 'erva '
nova_entrada = ''

for i in entrada:
    if [i] == ' ':
        nova_entrada.pop(i)
    else:
        nova_entrada += i

print(len(nova_entrada))






