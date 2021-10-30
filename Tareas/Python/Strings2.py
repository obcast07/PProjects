## Realizar un programa que comprueba si una cadena leída por teclado comienza por 
## una subcadena introducida por teclado.

cad1 = input("Ingrese una cadena: ")
cad2 = input("Ingrese una subcadena: ")

if cad1.startswith(cad2):
    print("La cadena inicia con la subcadena")
else: print("La cadena no incia con la subcadena")
