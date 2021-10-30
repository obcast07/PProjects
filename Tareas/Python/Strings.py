#Si tenemos una cadena con un nombre y apellidos, 
# realizar un programa que muestre las iniciales en mayúsculas.

i=0
nombre = input("Ingrese su nombre: ")
Mayus=nombre[i]
while i < len(nombre):
    if nombre[i]== " ":
        Mayus+=nombre[i+1]
        i+=1
    else: i+=1

print(Mayus.upper())



