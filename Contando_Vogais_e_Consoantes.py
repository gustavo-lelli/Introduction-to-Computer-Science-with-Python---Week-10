def conta_vogais(frase):
    vogais = frase.count('a') + frase.count('e') + frase.count('i') + frase.count('o') + frase.count('u') + frase.count('A') + frase.count('E') + frase.count('I') + frase.count('O') + frase.count('U')
    
    return vogais

def conta_letras(frase, contar = "vogais"):
    if contar == "consoantes":
        consoantes = len(frase) - frase.count(" ") - conta_vogais(frase)

        return consoantes
    else:
        return conta_vogais(frase)
