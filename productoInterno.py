##Código del producto interno
def productovectores(u,v,aMatriz):
    if(aMatriz.is_positive_definite() == True and aMatriz == aMatriz.transpose()):
        Producto = u*aMatriz*v
        return Producto
    else: 
        print("Debes ingresar una matriz simetrica y positiva definidad")
        return None
   
    r"""
    
    	DESCRIPCIÓN DE LA FUNCIÓN
	    *La función te regresa el producto interno de dos vectores dados, definido por una matriz dada
	
	Entrada (INPUT)
		
		*Un vector u, un vector v y una matriz aMatriz 
	Salida (OUTPUT)
		*Un número, el producto de u y v.
	
	Ejemplos: 
	
	Ejemplo 1
	
	v1 = vector([1,1]); v2 = vector([1,-1]); v = vector([8,-2])
    	B = (v1,v2)
    	A = identity_matrix(2)
    	print (productovectores(v1,v2,A))
    
    	Salida: 
       
    	0
	
	Ejemplo 2
	
	u = vector([2,3]); d = vector([1,2])
    	C = matrix(2,[1,-1, -1,1])
    
    	Salida: 
    
    	print (productovectores(u,d,C))
    
    	Debes ingresar una matriz simetrica y positiva definidad
	
	Authors: Jesus Santiago Fragoso Quintal, Luis Armando Valencia Serrano, Victor Eduardo Mendoza Solis, Ivan Farid
	    	 Espadas Escalante (2021 - 02 - 02)
    """
        
def ProyeccionOrtogonal(A,u,v):
    if(productovectores(u,v,A) != None and productovectores(u,u,A) != None):
        Componente = productovectores(u,v,A)/productovectores(u,u,A)
        Coeficiente = Componente * u
        return Componente, Coeficiente
    else:
        return None
    r"""
    
    	DESCRIPCIÓN DE LA FUNCIÓN
	    *Calcula la proyección ortogonal de u sobre v
	
	Entrada (INPUT)
		
		*A, u, v, donde A es una matriz, u, v son vectores. 
	Salida (OUTPUT)
		*(c, w), donde c es la componente de u a lo largo de v, o lo que es lo mismo, 
        el coeficiente de Fourier de u con respecto v; w es un vector, la proyección ortogonal 
        de u sobre v.
        
	Ejemplos: 
	u = vector([4,2]); d = vector([1,3])
   
    	A = identity_matrix(2)
    	print (ProyeccionOrtogonal(A,u,d))
    
    	Salida: 
    
    	(1/2, (2, 1))
	
	Authors: Jesus Santiago Fragoso Quintal, Luis Armando Valencia Serrano, Victor Eduardo Mendoza Solis, Ivan Farid
	    	 Espadas Escalante (2021 - 02 - 02)
    """

def ExpansionF(aMatriz, bBase, vVector):
    if(ProyeccionOrtogonal(aMatriz,bBase[0],vVector != None)):
        print("Combinación lineal:")
        print(" ")
        for i in range(len(bBase)-1):
            print(str(ProyeccionOrtogonal(aMatriz,bBase[i],vVector)[0])+"v"+str(i+1), end = ' + ')
        print(str(ProyeccionOrtogonal(aMatriz,bBase[i+1],vVector)[0])+"v"+str(i+2))
        print(" ")
        print("Coeficientes: ")
        print(" ")
        for i in range(len(bBase)-1):
            print(str(ProyeccionOrtogonal(aMatriz,bBase[i],vVector)[0]), end = ', ')
        print(str(ProyeccionOrtogonal(aMatriz,bBase[i+1],vVector)[0]))
    else:
        exit()
        
        r"""
    
    	DESCRIPCIÓN DE LA FUNCIÓN
	    *Calcula los coeficientes de Fourier de v, con respecto a la base ortogonal
	
	Entrada (INPUT)
		
		*A, B = {v1 , . . . , vr }, v, donde A es una matriz, B es un conjunto
    	ortogonal (ortogonal con respecto al producto que determina A), v un vector.
	
	Salida (OUTPUT)
		
		*c_1 , . . . , c_r , donde c_i es el coeficiente de Fourier de v con respecto a la
        base ortogonal.
        
	Ejemplo: 
	
	v1 = vector([1,1]); v2 = vector([1,-1]); v = vector([8,-2])
    	B = (v1,v2)
    	A = identity_matrix(2)
    	ExpansionF(A,B,v)
    
   	Salida: 
    
    	Combinación lineal:
 
    	3v1 + 5v2
 
    	Coeficientes: 
 
    	3, 5
	
	Authors: Jesus Santiago Fragoso Quintal, Luis Armando Valencia Serrano, Victor Eduardo Mendoza Solis, Ivan Farid
	    	 Espadas Escalante (2021 - 02 - 02)
    """
    
    
def GramS(aMatriz, bBase):
    Bp = [0]*len(bBase)
    cont = 0
    if(ProyeccionOrtogonal(aMatriz,Bp[0],bBase[0]) != None):
        for i in range(len(bBase)):
            if(i == 0):
                    Bp[0] = bBase[0]
            SumaP = 0
            for j in range(i):
                SumaP = SumaP - (ProyeccionOrtogonal(aMatriz,Bp[j],bBase[i])[1])
            Bp[i] = bBase[i] + SumaP
        return Bp
    else: 
        return None
    r"""
    
    	DESCRIPCIÓN DE LA FUNCIÓN
	    *Dado un conjunto linealmente independiente, aplica el proceso de ortogonalización de Gram - Schmidt
	
	Entrada (INPUT)
		
		*Entrada: A, B = {v 1 , . . . , v r }, donde A es una matriz, B es una colección de
        vectores linealmente independientes.
	Salida (OUTPUT)
		*B' = {v1', . . . , vr'}, donde B' es la lista de vectores que se obtiene al
        aplicar el proceso de Gram–Schmidt a la colección B.
        
	Ejemplos: 
       	v1 = vector([1,0,1]); v2 = vector([1,1,0]); v3 = vector([1,1,1])
       	B = (v1,v2,v3)
       	A = identity_matrix(3)
       	GramS(A,B)
       
       	Salida: 
       
       	[(1, 0, 1), (1/2, 1, -1/2), (-1/3, 1/3, 1/3)]
	
	Authors: Jesus Santiago Fragoso Quintal, Luis Armando Valencia Serrano, Victor Eduardo Mendoza Solis, Ivan Farid
	    	 Espadas Escalante (2021 - 02 - 02)
    """

