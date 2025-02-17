###
#02 - Bucles (for)
# permiten ejecutar un bloque de codigo repetidamente mientras ITERA un iterable o una lista
###


print("\nBucle for:")

#itera una lista
frutas=["manzana", "pera", "mandarina"]
for fruta in frutas:
    print(fruta)

#interar sobre cualquier ocsa que sea iterable
cadena ="mudidev"
for caracter in cadena:
    print(caracter)


# enumerate()
frutas = ["manzana", "pera", "orange"]

for index, fruta in enumerate(frutas):
    print(f"el indice es {index} y la fruta es {fruta}")


#bucles anidados
letras =["A", "B", "C"]
numeros=[1,2,3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")


#break
animales=["perro","gato","raton","loro","pez","canario"]
for idx, animal in enumerate(animales):
    print(animal)
    if animal =="loro":
        print(f"el loro esta escondido en el indice {idx}")
        break

# continue
print("\ncontinue:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
  if animal == "loro": continue
  
  print(animal)

# Comprensión de listas (list comprehension)
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# Muestra los números pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pares)

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
numeros= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for numero in numeros:
    if numero %2 == 0: 
        print(numero)





# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

suma=0
for numero in numeros:
    suma = numero + suma
media=suma/len(numeros)
print(media)    



# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
aux=0
for num in numeros:
    if num > aux:
        aux = num
print(aux)        


# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

palabrasMas5 = [palabra for palabra in palabras if len(palabra)>5 ]
print(palabrasMas5)





# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")

letra = input("cual letra corroborramos en la lista para ver??")
if len(letra) != 1:
    print("Por favor, ingresa solo una letra.")
else:
    letra = letra.lower()  # Convertimos la letra a minúscula


contador=0
for palabra in palabras:
    if palabra[0].lower() == letra:
        contador+=1

print(f"hay {contador} palabras que coinciden con la letra {letra} elegida")