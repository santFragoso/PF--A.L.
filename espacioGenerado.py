P.<a,b,c,d>=QQ[]
v1 = vector([1,-1,2,1]); v2 = vector([-1,1,1,2]); v3 = vector([0,0,3,3]); v4 = vector([2,-2,1,-1])
VectorGen = ([a,b,c,d])
nv1 =[]; nv2 =[]; nv3 =[]; nv4 =[]
W = (v1,v2,v3,v4)
print(W)
j=0
for i in range (0,4):
    nv1.append(W[i][j])
nv1.append(a)
j=j+1
for i in range (0,4):
    nv2.append(W[i][j])
nv2.append(b)
j=j+1
for i in range (0,4):
    nv3.append(W[i][j])
nv3.append(c)
j=j+1
for i in range (0,4):
    nv4.append(W[i][j])
nv4.append(d)

print(nv1)
print(" ")
print(nv2)
print(" ")
print(nv3)
print(" ")
print(nv4)
print(" ")

A = matrix(P,4,5, [nv1, nv2, nv3, nv4])
print(A)
print(" ")

AER = A.echelon_form('row_reduction')
print(AER)

print(" ")
print(AER[2][4])
print(AER[3][4])
