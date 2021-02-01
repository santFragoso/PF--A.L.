def conjGenTipo1(matrizDeRelaciones):
  matrizRREF = matrizDeRelaciones.rref()
    
  m,n = matrizDeRelaciones.dimensions()
  columnasPivote = matrizRREF.pivots() 
  
  numColumnasPivote = len(columnasPivote)
    
  numConjuntoGen = n - numColumnasPivote
  cardinalidadVectores = n 
  conjuntoVectoresGen = Matrix(QQ, numConjuntoGen, cardinalidadVectores) ##las filas son los vectores
  
  listaConjuntoGenerador = []
   
  restar = 0  
  for i in range(0, n):
    ##copiamos la columna en negativo (numColumnasPivote + i) del rref en la fila que le corresponde
    filaTemporal = [0]*n
    y=0
    for z in columnasPivote:
        if (i == z):
            y = 1
            
    if (y == 1):
        restar = restar+1
        continue
        
    
    for j in range(0,m):
      filaTemporal[j] = -( matrizRREF[j,i] )
    ##Antes de cambiar de fila(vector) agregamos los 0 pertinentes  
    for k in range(0, n - numColumnasPivote):
      filaTemporal[numColumnasPivote + k] = 0
    
    
    
    filaTemporal[numColumnasPivote + i - restar ] = 1 ##Agregamos el 1 donde corresponde
    listaConjuntoGenerador.append(filaTemporal)
    
    
  

    
  
  return listaConjuntoGenerador

def conjGenTipo2():
  pass


def conjGenTipo3():
  pass


def conjuntoGenerador(matrizDeRelaciones, tipo, dimMConjGenMatriz, dimNConjGenMatriz): 
  if (tipo == 1):
    print(conjGenTipo1(matrizDeRelaciones))
    
  if (tipo == 2):
    conjGenTipo2(matrizDerelaciones)
  
  if (tipo == 3):
    conjGenTipo3(matrizDerelaciones, dimMConjGenMatriz, dimNConjGenMatriz)
    
  pass  
 
  
  


##Datos para ejecutar ejemplos:
matrizDeRelaciones = Matrix([[1,2,0,3],[0,0,1,-1],[0,0,2,-2],[0,0,2,-2]])
tipo = 1 
conjuntoGenerador(matrizDeRelaciones, tipo, 0, 0)
