def maiusculas(frase):
    uppers = ''
    for i in range(len(frase)):
        if frase[i] >= 'A' and frase[i] <= 'Z':
            uppers += frase[i]

    return uppers
