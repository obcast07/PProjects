#Tuplas
# 1.- Crear una variable flotante, integer, boleana y compleja e imprimir el tipo de varibale que es

var1 = 15.67
var2 = 15
var3 = True
var4 = 1+ 5j

print("Var 1 es ", type(var1))

print("Var 2 es ", type(var2))
print("Var 3 es ", type(var3))
print("Var 4 es ", type(var4))

# 2.- Crear una tupla con valores enteros imprimir el primer y ultimo valor

b= (1,2,3,4,5,6)



print("El primer y último número son: ",b[0]," y ", b[-1])

# 3.- Añadir 3 valores de string a la tupla
# Hay 2 maneras, la primera es crear una tupla con los strings y concatenar
b= (1,2,3,4,5,6)

c= ("Anita","lava la", "tina")

b=b+c

print(b)

# 4.- Verificar si una variable existe dentro de una tupla


b= (1,2,3,4,5,6)

c= ("Anita","lava la", "tina")

a=b+c

if 4 in c:
    print("True")
else: print("false")

