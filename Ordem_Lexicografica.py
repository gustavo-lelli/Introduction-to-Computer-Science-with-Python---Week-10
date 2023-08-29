def primeiro_lex(vector):
    first = vector[0]

    for i in range(1, len(vector)):
        if first.lower() > vector[i].lower():
            first = vector[i]

    return first


print(primeiro_lex(['A', 'a', 'casa']))
