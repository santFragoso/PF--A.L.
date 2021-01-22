##código para el conjunto generador



def conjGenTipo1(matrizDeRelaciones):
  matrizRREF = matrizDeRelaciones.rref()
  m,n = matrizDeRelaciones.dimensions()
  columnasPivote = matrizRREF.pivots() 
  numColumnasPivote = len(columnasPivote)
  numConjuntoGen = n - numColumnasPivote
  cardinalidadVectores = m + numColumnasPivote
  conjuntoVectoresGen = Matrix(numConjuntoGen, cardinalidadVectores) ##las filas son los vectores
  
  for i in range(0, numConjuntoGen):
    ##copiamos la columna en negativo (numColumnasPivote + i) del rref en la fila que le corresponde
    for j in range(0,m):
      conjuntoVectoresGen[i, j] = -( matrizRREF[j, numColumnasPivote + i] )
    ##Antes de cambiar de fila(vector) agregamos los 0 pertinentes  
    for k in range(0, numColumnasPivote):
      conjuntoVectoresGen[i,m + k] = 0
    conjuntoVectoresGen[i, m + i] = 1 ##Agregamos el 1 donde corresponde
  
  listaConjuntoGenerador = []
  for l in range(0, numConjuntoGen):
    listaConjuntoGenerador.append(conjuntoVectoresGen[l])
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
matrizDeRelaciones = Matrix([[1,2,-1,3],[3,5,-4,7]])
tipo = 1 
conjuntoGenerador(matrizDeRelaciones, tipo, 0, 0)

                 
               
