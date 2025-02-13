###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

contador=10
while contador >0:
    print(contador)
    contador-=1





# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
contador=1
suma = 0
while contador <=20:
    if contador %2==0:
        suma+=contador
    contador+=1

print(suma)


# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo 
# es el producto de todos los números del 1 al ese número. 
# Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
numero_introducido= int(input("Introduce un numero positivo"))

if numero_introducido < 0:
    print("debes introducir un numero positivo")
else:
    factorial =1
    contador=numero_introducido

    while contador >0:
        factorial*=contador
        contador-=1    


print(f"el factorial del {numero_introducido} es {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta
#  que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

print("generador de contraseña")
print("crea tu contraseña de 8 caracteres")
contrasena=input("introduce aqui la primer contraseña\n")

while len(contrasena)<8:
    
    print("has ingresado una contraseña de menos cacteres que los oslicitados")
    contrasena=input("introduce aqui nuevamente\n")

print(f"se ha validado la contraseña y es {contrasena}")



# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

print("tablas de multiplicar")
numero=int(input("introduce un numero para saber su tabla de multi\n"))
while numero >=10 or numero<0:
    numero=int(input("introduce un numero entre 1 y 10\n"))
else:
    print(f"has introducido \n{numero}")


contador=1
while contador<=10:
    resultado=numero*contador
    print(f"{numero} * {contador} = {resultado}")
    contador+=1



# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
