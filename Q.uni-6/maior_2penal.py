def maior_penal(nomes, idades):
    maiores = ''
    for i in range(len(nomes)):
        if int(idades[i]) >= 18:
            maiores += nomes[i] + ' '

    maiores_2 = ''
    for i in range(len(maiores)):
        if maiores[i] == maiores[i]:
            maiores_2 += maiores[i]
        if maiores[i+1] == ' ':
            maiores_2 += '$'

    print(maiores_2)     
    print(len(maiores))
    
    return maiores  

nomes = input().split()
idades = input().split()
print(maior_penal(nomes, idades))
