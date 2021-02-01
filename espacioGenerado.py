##código para el espacio generado

def espacioGenerado(W):
   
    m = len(W[0])
    n = len(W)
        
    A = matrix(m,n+1)
    for i in range(0,m):
        for j in range(0,n):
            A[j,i] = W[i][j]
    return A

v1 = vector([1,-1,2,1]); v2 = vector([-1,1,1,2]); v3 = vector([0,0,3,3]); v4 = vector([2,-2,1,-1])
W = (v1,v2,v3,v4)
print(espacioGenerado(W))
espacioGenerado(W)
C=[]
x1 = var('x1'); x2 = var('x2'); x3 = var('x3'); d = var('x4')
var('a b c d')
VectorGen = ([a,b,c,d])
Variables = ([x1,x2,x3,x4])
print(VectorGen)
print(" ")
for i in range (0,len(W)):
    C.append(Variables[i]*W[i])
print(C)
print(" ")

Eq=[]
for i in range(0, len(W)):
    valor=0
    for j in range (0, len(W)):
        valor = valor + C[j][i]
    Eq.append(valor)

print(" ")
print(Eq)

EPR=[]
for i in range (0,len(W)):
    EPR.append(Eq[i]==VectorGen[i])
    
print(" ")
print(EPR)
print(" ")
solve(EPR,Variables)
