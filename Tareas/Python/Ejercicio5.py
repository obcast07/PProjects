import funciones

print("Ingrese 2 números: ")
a=int(input("Primer número: "))
b=int(input("Segundo número: "))

print("Elige la operación.")

print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.División")
print("5.Exponentes")

while True:
    opc = input("Ingresa la opcion (1|2|3|4|5): ")
    if opc in ('1','2','3','4','5'):
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))

        if opc =='1':
            print(num1, "+", num2, "=", funciones.suma(num1,num2))

        elif opc == '2':
            print(num1, "-", num2, "=", funciones.resta(num1, num2))
        
        elif opc == '3':
            print(num1, "*", num2, "=", funciones.multi(num1, num2))

        elif opc == '4':
            print(num1, "/", num2, "=", funciones.div(num1, num2))
        elif opc == '5':
            print(num1, "**", num2, "=", funciones.exp(num1,num2))
        
        else: print("opcion inválida")
            
            