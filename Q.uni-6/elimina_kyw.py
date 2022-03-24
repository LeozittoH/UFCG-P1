def elimina_kyw(sentenca):
    
    nova_sentenca = ''    
    i = 0
    while True:
        if sentenca[i] == 'k':
            nova_sentenca += ''
        elif sentenca[i] == 'y':
            nova_sentenca += ''
        elif sentenca[i] == 'w':
            nova_sentenca += ''
        else:
            nova_sentenca += sentenca[i]    
        i += 1
        if i >= len(sentenca): break
    
    return nova_sentenca

s1 = 'kasayeww'
s2 = 'makria bonita'  
s3 = 'kekw'
s4 = 'kenon'
s5 = 'ykoiwwl'   

assert elimina_kyw(s3) == 'e'
assert elimina_kyw(s4) == 'enon'
assert elimina_kyw(s5) == 'oil'