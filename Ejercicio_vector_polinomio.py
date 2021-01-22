import numpy as np  
def fun(A):
    len_A=len(A)
    n=len_A-1
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
        polinomio = fun(my_vector_actual)
        print(polinomio)

if __name__ == "__main__":
    A=np.array(([3,9,7,5,76,329]))
    B=np.array(([1,2,3]))
    #Opcion 1
    print("imprimir vectores\n")
    print(fun(A))
    print(fun(B))
    ###EXTENSION CODIGO A LISTA DE VECTORES
    #Opcion 2
    mi_lista=[A,B]
    print("imprimir lista de vectores\n")
    pasar_lista_vectores(mi_lista)