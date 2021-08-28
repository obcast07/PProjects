import math

#Definimos la función que genera los valores
def gen_linear(a, x, b , m):
    #definimos res como string que será llenada con los valores generados

    res=""

    for i in range(0,x):
        #fórmula
        val = (a * x + b) % m
        #concatenación de resultados en res
        res += str(val) + " "
        #lo de arriba es igual a res = res + str(val)
        x = val;
        #toma el valor del numero pasado, de la iteración pasada
    return (res) #regresa la cadena res una vez terminada la función


#main, declararion de variables
a= int(input("Ingresa el valor de a: "))
X0 = int(input("Ingrese el valor de X0: "))
b = int(input("Ingrese el valor de b: "))
m= int(input("Ingrese el valor de m: "))

#llamando la función definida anteriormente
res=gen_linear(a,X0,b,m)

print(res)

