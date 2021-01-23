##Código del producto interno
def productovectores(u,v,MatrizP):
    if(MatrizP.is_positive_definite() == True and MatrizP == MatrizP.transpose()):
        Producto = u*MatrizP*v
        return Producto
    else: 
        print("Debes ingresar una matriz simetrica y positiva definidad")
        return None
        
def ProyeccionOrtogonal(A,u,v):
    if(productovectores(u,v,A) != None and productovectores(u,u,A) != None):
        Componente = productovectores(u,v,A)/productovectores(u,u,A)
        Coeficiente = Componente * u
        return Componente, Coeficiente
    else:
        return None

def ExpansionF(aMatriz, bBase, vVector):
    if(ProyeccionOrtogonal(aMatriz,bBase[0],vVector != None)):
        for i in range(len(bBase)-1):
            print(str(ProyeccionOrtogonal(aMatriz,bBase[i],vVector)[0])+"v"+str(i+1), end = ' + ')
        print(str(ProyeccionOrtogonal(aMatriz,bBase[i+1],vVector)[0])+"v"+str(i+2))
    else:
        exit()
    
    
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
