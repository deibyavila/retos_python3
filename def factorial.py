def factorial(n):
    resultado = ""
    for i  in range(1,n):
       resultado = resultado + str(i)
    resultado += str(n)
    return resultado
 
#CALCULAMOS EL FACTORIAL DE 5.
print(factorial(3))
 
