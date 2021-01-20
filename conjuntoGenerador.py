##código para el conjunto generador







def conjuntoGenerador(matrizDeRelaciones, tipo):
  matrizRREF = matrizDeRelaciones.rref()
  m, n = matrizDeRelaciones.dimensions()
  cardinalidadConjuntoGen = n - len(matrizRREF.pivots)
  conjuntoVectoresGen = [None] * cardinalidadConjuntoGen
  for i in range(1, cardinalidadConjuntoGen):
    for j in range(0, n):
      ##agarra cada elemento de la columna y copiarlo en un array que despues debe ser metido en el arreglo
      ## conjuntoVectoresGen
      
  ## Cada vector es de longitud n, la cual debe corresponder a las columnas de la matriz
  pass


##Datos para ejecutar ejemplos:
matrizDeRelaciones = Matrix([[1,2,-1,3],[3,5,-4,7]])
tipo = 1 
conjuntoGenerador(matrizDeRelaciones, tipo)
