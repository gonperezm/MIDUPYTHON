###
#01 - Bucles (while)
# Perminten ejecutar un bloque de codigo repetidamente mientras se cumpla la condicion
###

print("Bucle while:")

#Bucle con una simple condicion
contador=0

while contador <=5:
    print(contador)
    contador += 1 # es super importante para evitar un bucle infinito

#utilizando la palabra break para romper el bucle
print("Bucle con break")
contador=0

while True:
    print(contador)
    contador=+1
    if contador ==5:
        break #sale del bucle

#continue, que lo hace es saltar esa iteracion en concreto

print("Bucle con continue")
contador=0
while contador<10:
    contador=+1

    if contador %2 ==0:
        continue
    print(contador)


#else, esta condicion cuando se ejecuta?

print("Bucle while con else:")
contador=0
while contador < 5:
    print(contador)
    contador=+1
else:
    print("el bucle ha termninado")   

#pedirle al usuario un numero y que tiene q ser positivo

numero = -1
while numero <0:
    numero=int(input("introduce un numero positivo"))
    if numero<0:
        print("el numero no es positivo")     

print(f"el numero q has elegido es {numero}")        
#esto de arriba es la forma basica pero sin TRY CATCH(EXCEPT)


numero = -1
while numero < 0:
    try:
        numero=int(input("introduce un numero positivo"))
        if numero<0:
            print("el numero no es positivo")     
    except:
        print("lo que introduces debe ser un numero sino bugggg")


print(f"el numero q has elegido es {numero}")


