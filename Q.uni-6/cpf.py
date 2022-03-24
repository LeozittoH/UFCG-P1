def calcula_digitos_verificacao(cpf):
    
    verificador = ''
    mult = 2
    resultado = 0
    for i in range(len(cpf)-1, -1, -1):
        calculo = int(cpf[i]) * mult
        resultado += calculo
        mult += 1
    resultado = str((10 * resultado) % 11)
    verificador += resultado

    mult = 2
    resultado = 0
    for i in range(len(cpf)):
        calculo = int(cpf[i]) * mult
        resultado += calculo
        mult += 1
    resultado = str((10 * resultado) % 11)
    verificador += resultado
    
    return verificador


cpf = '153245875'
cpf1 = '111111111'
cpf2 = '394857239'
print(calcula_digitos_verificacao(cpf))
print(calcula_digitos_verificacao(cpf1))
print(calcula_digitos_verificacao(cpf2))

assert calcula_digitos_verificacao('153245875') == '40'
assert calcula_digitos_verificacao('111111111') == '11'

    