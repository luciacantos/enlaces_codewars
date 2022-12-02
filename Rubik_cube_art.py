def cube(n):
    #lista
    superior = []
    #bucle para el trozo superior del cubo
    for x in range(n):
        superior.append(" " * (n-x-1) + "/\\" * (x+1) + "_\\" * n)
    #lista
    inferior = []
    #bucle para el trozo inferior del cubo
    for x in range(n):
        inferior.append(" " * x + "\\/" * (n-x) + "_/" * n);
    # une las listas y dibuja el cubo entero
    cubo = superior + inferior
    return "\n".join(cubo)
