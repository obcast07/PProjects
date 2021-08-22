i=0
lista=[]
while i<10:
    numero= int(input("Ingrese un numero multiplo de 3: ")) 
    if numero%3 == 0:
        lista.append(numero)
        i=i+1
    else :print("No es multiplo de 3")

print("los numeros ingresados fueron: ",lista)

sumatoria=0
for num in lista: 
    sumatoria += num

print("la suma de los numeros es: ",sumatoria)

       
