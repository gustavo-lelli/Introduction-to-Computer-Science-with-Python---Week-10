def strip_and_capitalize(nomes):
    for i in range(len(nomes)):
        nomes[i] = nomes[i].strip()
        nomes[i] = nomes[i].capitalize()

    return nomes

def menor_nome(nomes):
    nomes = strip_and_capitalize(nomes);
    menor = nomes[0]
    for i in range(len(nomes)):
        if len(menor) > len(nomes[i]):
            menor = nomes[i]

    return menor


nomes = ['zé', ' lu', 'fê']
print(menor_nome(nomes))
