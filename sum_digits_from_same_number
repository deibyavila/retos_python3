"""
ESTE RETO CONSISTE EN TENER DOS FLUJOS DE DATOS QUE DEBE CRECER DADA LA SUMA DE SI MISMO MAS LA SUMA DE LOS DIGITOS QUE LO COMPONEN,
MATEMATINCAMENTE ESTOS NUMERO SE VA A ENCONTRAR EN ALGUN PUNTO POR ENDE SE DEBE DE RETORNAR DICHO PUNTO DE ENCUENTRO
"""
def getS_1(n): 
    
    sum = 0
    while (n!=0):  
                
        sum = sum + int(n % 10) 
        n = int(n/10)
                   
    return sum

def full(fun):
    val =[]
    x= 0
    if x ==0:
        x=fun
    while(True):
        x= x + getS_1(x)
        val.append(x)
        if x>2000:
            break
    return val

#print(full(471)) #492

#print(full(480))

def compute_join_point(s_1, s_2):
    x = full(s_1)
    y = full(s_2)
    joddin=0
    for i in x:
        for v in y:
            if i==v:
               
                joddin = v
                break
        if i==joddin:
            break    
    return joddin
  

print(compute_join_point(471,480)) 
