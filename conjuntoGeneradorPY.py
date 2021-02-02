import numpy as np

def vector_Polinomio(A):
    len_A=len(A)
    n = len_A-1
    chain=""
    for k in range(len_A):   
        if   k == 0:
            chain = chain+str(A[k])
        elif k == 1:
            chain = chain + "+"  + str(A[k])+ "t"
        else: 
            chain = chain + "+" + str(A[k]) + "t^"+str(k)
    return chain

def pasar_lista_vectores(lista_vectores):
    tamano_lista_vectores = len(lista_vectores)    
    for k in range(tamano_lista_vectores):
        my_vector_actual = lista_vectores[k]
        polinomio = vector_Polinomio(my_vector_actual)
        print(polinomio)
        
def imprimirVectorEnMatriz(listaVectores,m,n):
    B = Matrix(m,n)
    listaMatrices = []
    
    for i in range (0,len(listaVectores)):
        B = Matrix(QQ, m,n)
        for k in range (0, m):
            for j in range (0,n):
                B[k,j] = listaVectores[i][((k*n) + (j+1)) - 1]
                
        listaMatrices.append(B)
        
       
    print(" ")
    print(listaMatrices)
    return
           
def conjuntoGenerador(A, tipo, dimMConjGenMatriz, dimNConjGenMatriz):
   
    if (tipo>3 or tipo<1):
        return "ERROR, tipo no válido"
    m,n = A.dimensions()
    print(" ")
    AER = A.rref()
    
    Mayor = max(m,n)
    B = identity_matrix(Mayor)
    AN =matrix(Mayor,Mayor)
    print(" ")

    for i in range (0,Mayor):
        for j in range (0,Mayor):
            if (i<m):
                AN[i,j]=A[i][j]
            if (i>m):
                AN[i,j]=0
    
    ARN = AN.rref()
    CG = ARN - B   
    ColumnasCG = CG.columns()   
    ListCG=[]
    for i in range (0, Mayor):
        if (ColumnasCG[i][0]!=0):
            ListCG.append(-1*ColumnasCG[i])
        
   
    
    if (tipo==1):
        print(ListCG)
    elif(tipo==2):
        pasar_lista_vectores(ListCG)
    elif(tipo==3):
        if (dimMConjGenMatriz == 0 or dimNConjGenMatriz == 0):
            return "ERROR: ingrese dimensiones mayores a 0"
        if (dimMConjGenMatriz * dimNConjGenMatriz != n):
            return "ERROR: las dimensiones dada para las matrices no son compatibles con las dimensiones de la matriz de relaciones"
        else:
            imprimirVectorEnMatriz(ListCG,dimMConjGenMatriz, dimNConjGenMatriz)
       
        
r"""
    
    	DESCRIPCIÓN DE LA FUNCIÓN
	    *Te regresa un conjunto generador para un subespacio, el cual está definido
	    por una matriz de relaciones dada
	
	Entrada (INPUT)
		*Una matriz de relaciones
		*Un número para indicar el tipo de subespacio(1 subespacio de R^n, 2 subespacio de polinomios, 3 subespacio de matrices).
		*El tamaño de la matriz cuando se trata de subespacios de tipo 3. 
	Salida (OUTPUT)
		*Un conjunto generador para el subespacio
	
	*Nota:
	
        *En el caso de matrices, el producto de las dimensiones dadas tiene que ser igual al numero de columnas de la matriz de relaciones, 
        de lo contrario, el programa regresará un error
        *igualmente, no se admiten dimensiones <1
        *En caso de no requerir matrices, se puede ingresar cualquier numero en los apartados de dimensiones de las matrices, 
        es decir que si es tipo 1 o tipo 2, los dos ultimos valores son irrelevantes pero deben ingresarse
	
	Ejemplos: 
	
	Ejemplo 1 con subespacios tipo 1 (vectores)
	
	B = matrix(QQ,2,2,[1,3,2,6])

	print("Matriz de relaciones dada: \n",B)
	conjuntoGenerador(B, 1,0,0)
    
    	Salida: 
    
    	Matriz de relaciones dada: 
 	[1 3]
	[2 6]

	[(-3, 1)]
	
	Ejemplo 2 con subespacios tipo 2 (polinomios):
	
	B = matrix(QQ,2,2,[1,3,2,6])

	print("Matriz de relaciones dada: \n",B)
	conjuntoGenerador(B, 2,0,0)
    
    	Salida: 
    
    	Matriz de relaciones dada: 
 	[1 3]
	[2 6]
	
	3+-1t+1t^2+0t^3
	1+-2t+0t^2+1t^3
	
	Ejemplo 3 con subespacios tipo 3 (matrices)
	
	A = matrix(QQ,2,4,[1,2,-1,3,3,5,-4,7])
	print("Matriz de relaciones dada: \n",A)
	conjuntoGenerador(A, 3, 2, 2)
    
    	Salida: 
       
    	Matriz de relaciones dada: 
    	
	[ 1  2 -1  3]
	[ 3  5 -4  7]
 
 
	[[ 3 -1] [ 1 -2]
	 [ 1  0],[ 0  1]] 
	
	
	
	
	
	Authors: Jesus Santiago Fragoso Quintal, Luis Armando Valencia Serrano, Victor Eduardo Mendoza Solis, Ivan Farid
	    	 Espadas Escalante (2021 - 02 - 02)
    """
    
    
A = matrix(QQ,2,4,[1,2,-1,3,3,5,-4,7])
print("Matriz de relaciones dada: \n",A)
conjuntoGenerador(A, 3, 2, 2)
