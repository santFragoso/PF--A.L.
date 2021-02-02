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
    #print("control")
    #print(listaVectores[0])
    
    for i in range (0,len(listaVectores)):
        B = Matrix(QQ, m,n)
        for k in range (0, m):
            for j in range (0,n):
                B[k,j] = listaVectores[i][((k*n) + (j+1)) - 1]
                
        listaMatrices.append(B)
        
       
    print(" ")
    print(listaMatrices)
    return
           
        
    
    
    

#if __name__ == "__main__":
 #   A=np.array(([3,9,7,5,76,329]))
#    B=np.array(([1,2,3]))
    #Opcion 1
  #  print("imprimir vectores\n")
   # print(vector_Polinomio(A))
    #print(vector_Polinomio(B))
    ###EXTENSION CODIGO A LISTA DE VECTORES
    #Opcion 2
    #mi_lista=[A,B]
    #print("imprimir lista de vectores\n")
    #pasar_lista_vectores(mi_lista)

def conjuntoGenerador(A, tipo, dimMConjGenMatriz, dimNConjGenMatriz):
    #A = matrix(QQ,2,2,[1,3,2,6])
    #print(A)
    
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
       
        

    
    
A = matrix(QQ,2,4,[1,2,-1,3,3,5,-4,7])
print("Matriz de relaciones dada: \n",A)
conjuntoGenerador(A, 3, 2, 2) # A es la matriz, 3 es el tipo, 2,2 son las dimensiones que corresponden al tipo 3, matrices
                                #el producto de las dimensiones dadas tiene que ser igual al numero de columnas de la matriz de relaciones
                                #de lo contrario, el programa regresará un error
                                #igualmente, no se admiten dimensiones <1
                                #en el caso de que no se requieran matrices, se pueden ingeresar cualquier numero
                                # es decir que si es tipo 1 o tipo 2, los dos ultimos valores son irrelevantes pero deben ingeresarse
