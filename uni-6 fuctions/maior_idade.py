def maioridade_penal(nomes, idades):
    nomes = nomes.split()
    idades = int(idades).split()
    maiores = ''

    for i in range(len(idades)):
        if (idades[i]) >= 18:
            maiores.append(nomes[i])
    
    return maiores
    
print(maioridade_penal("leonam iasmym david joyce ", "18 17 18 16"))
print(maioridade_penal("leonam iasmym david joyce ", "0 0 0 0"))
#assert maioridade_penal("leonam iasmym david joyce", "19 2 18 0") == "leonam david "



