"""
ESTE RETO CONSISTE EN DADA UNA ARRAY DE NUMERO Y UN NUMERO A BUSCAR, VALIDAR SI DICHO NUMERO A BUSCAR SE ENCUENTRA EN LA SET DE NUMERO ENTREGADOS
Y ADICIONALMENTE VALIDAR SI LA POSICION EN LA QUE SE ENCUENTRA ES PAR"""
def is_on_even_position(table, value):
    # Your code goes here
salida = False
    for i in range(len(table)):
        
        if table[i] == value and (i%2==0 )== True or i==0:
            salida = True
       
    return salida


t = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(is_on_even_position(t, 6))  
print(is_on_even_position(t, 3)) 
