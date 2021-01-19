def crearMatrizAsociada(AMatriz, BVector):  ##Crea una sola matriz a partir de la matriz A y el vector B
    m, n = AMatriz.dimensions()
    matrizAsociada = matrix(m, n + 1)
    for i in range(0, m):
        matrizAsociada[i, n] = BVector[i]
        for j in range(0, n):
            matrizAsociada[i, j] = AMatriz[i, j]
    print(matrizAsociada)
    return matrizAsociada


def determinadaOIndeterminada(AMatriz):  ##verrifica si el sistema es determinado o indeterminado y regresa 1 o 2 dependiendo del caso
    m, n = AMatriz.dimensions()
    rangA = AMatriz.rank()

    if (rangA == n):
        print("Es un sistema determinado")
        return 1
    else:
        print("Es un sistema indeterminado")
        return 2


def variablesLibyBasEnLib(MatrizRREF):  ##Determina las variables libres, las imprime e imprime las basicas con base en las libres
    pivRREF = (MatrizRREF.pivots())
    NB = max(MatrizRREF.pivots())
    Mxi, Mxk = MatrizRREF.dimensions()

    print("Variables libres:")
    for i in range(NB + 1, Mxk - 1):
        print("x", i)
    print("Variables básicas en términos de libres:")

    for i in range(0, Mxi):
        print("x", pivRREF[i], end=" = ")
        for k in range(NB + 1, Mxk - 1):
            print("(", -MatrizRREF[i, k], ")", "x", k, end="  +  ")
        print("(", MatrizRREF[i, k + 1], ")")


def tieneSolucion(matrizRREF, AMatriz):  ##determina si el sistema tiene solucion o si no, retorna un valor que indica esto
    rangMAum = matrizRREF.rank()
    rangA = AMatriz.rank()

    if (rangMAum != rangA):
        print("No tiene solución")
        return 0
    else:
        print("Si tiene solución")
        return 1


def SolConsistDet(MatrizRREF):
    Mxi, Mxk = MatrizRREF.dimensions()
    k = Mxk
    pivRREF = MatrizRREF.pivots()
    print("Las variables básicas son")

    for i in (pivRREF):
        print("x", pivRREF[i], end=" = ")
        print(MatrizRREF[i, k - 1])


def calcularDetalles(matrizRREF, AMatriz):
    tipo=0
    tipo = determinadaOIndeterminada(AMatriz)  ##Imprime que tipo es y retorna 1 o 2 dependiendo de si esdeterminada o indeterminada
    print("Forma escalonada reducida por renglones: ")
    print(matrizRREF)
    ##
    pivotes = matrizRREF.pivots()
    print("Las variables pivotes son las siguientes: ")
    d = len(pivotes)
    for i in range(0, d):
        print("x", pivotes[i])
    
    ##
    if tipo == 2:
        variablesLibyBasEnLib(matrizRREF)
    else:
        SolConsistDet(matrizRREF)


##esta es la funcion que debemos llamar para iniciar el programa, igual contendrá la descripción
def resolverSistema(AMatriz, BVector):
    r"""
    

    """
    m, n = AMatriz.dimensions()
    magnitudBVector = len(BVector)
    print(magnitudBVector)

    if (magnitudBVector == m):
        matrizAsociada = crearMatrizAsociada(AMatriz,BVector)  ##Creamos una matriz única como la matriz asociada [AMatriz|BVector] para obtener la RREF con rref()
        matrizRREF = matrizAsociada.rref()  ##se almacena la RREF en una variable para evitar repetir su cálculo
        if (tieneSolucion(matrizRREF, matrizAsociada) == 1):
            calcularDetalles(matrizRREF, AMatriz)
        else:
            print("El sistema de ecuaciones no tiene solución")
    else:
        print("Las dimensiones de la matríz y del vector no son compatibles")


a = matrix(3, [2, 2, 4, 7, 6, 8]);
b = vector([1, 2, 3]);
resolverSistema(a, b)
