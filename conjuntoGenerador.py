##código para el conjunto generador

def conjGenTipo1(matrizDeRelaciones):
  matrizRREF = matrizDeRelaciones.rref()
  m, n = matrizDeRelaciones.dimensions()
  columnasPivote = matrizRREF.pivots()
  cardinalidadPivotes = len(columnasPivote)
  cardinalidadConjuntoGen = n - len(columnasPivote)
  conjuntoVectoresGen = [None] * cardinalidadConjuntoGen
  elementosPorVector = m + cardinalidadPivotes
  vectorTemporalConjuntoGen = Matrix(elementosPorVector)
  for i in range(0, cardinalidadConjuntoGen):
    for j in range(0, m):
      vectorTemporalConjuntoGen[j] = matrizRREF[j, cardinalidadPivotes + (i-1)]
     ## conjuntoVectoresGen[i-1] = matrizRREF[j, cardinalidadPivotes + (i-1)]
    for k in range(0, n - cardinalidadPivotes - 1):
      vectorTemporalConjuntoGen[m+k] = 0  ##ponemos los 0 restantes
      
    vectorTemporalConjuntoGen[m+(i)] = 1  ##ponemos el 1 correspondiente
    conjuntoVectoresGen[i] = vectorTemporalConjuntoGen
  
  return conjuntoVectoresGen
      
      
      ##agarra cada elemento de la columna y copiarlo en un array que despues debe ser metido en el arreglo
      ## conjuntoVectoresGen
      
  ## Cada vector es de longitud n, la cual debe corresponder a las columnas de la matriz
  pass
  pass


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

                 
               
