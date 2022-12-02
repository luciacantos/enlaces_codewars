def alphabet_war(fight):
    #inicializas el contador para cada lado
    contador_i = 0
    contador_d = 0

    #diccionario con las letras y sus valores
    izquierda = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    derecha = {'m': 4, 'q': 3, 'd': 2, 'z': 1}

    #sumar el valor de cada letra dependiendo del lugar en el que esté
    #si no está en ningún lado no suma nada
    for i in fight:
        if i in izquierda:
            contador_i += izquierda[i]
        elif i in derecha:
            contador_d += derecha[i]

    #ver el resultado
    if contador_i < contador_d:
        return "Right side wins!"
    elif contador_i > contador_d:
        return "Left side wins!"
    else:
        return "Let's fight again"
