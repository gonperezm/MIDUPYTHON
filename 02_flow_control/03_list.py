###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

import os
os.system("clear")

#creacion de listas

print("\n Crear listas")
lista1=[1, 2, 3,4,5] #lista de entero
lista2=["manzana","pera","platano"]#lista de cadena
lista3=[1,"manzana",3.14, True] #lista de tipos

lista_vacia=[]
lista_de_listas = [[1,2],[3,4]]
matrix = [[1,2],[3,4], [5,6]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)


# Acesso a elementos por indice
print("\n Acceso a elementos por indice")
print(lista2[0]) #manzanas
print(lista2[1]) #peras
print(lista2[-1]) #platanos
print(lista2[-2]) #peras

print(lista_de_listas[1][0])


#slicing de listas
lista1=[1, 2, 3,4,5,6,7,8,9,10,11,12,13,14]

print(lista1[1:4]) #[2,3,4]
print(lista1[:3])#los primeros
print(lista1[3:]) #los finales

print(lista1[:])#hace una copia

#hay mas!!!
#para revertir la lista

#print(lista1[desde:hasta:paso])#???

print(lista1[::2]) #hazme una copia, hasta el final pero con los indice de 2 en 2
#quedaria [1,3,5,7,9,etcetc
print(lista1[::-1])#hazme una copia hasta el final pero de forma revertida

#MODIFICAR UNA LISTA

lista1[0] = 20
print(lista1)

#añadir elementos a una lista
#op1
lista1 =[1,2,3]
lista1 = lista1 + [88,99,55]
print(lista1)
#op2
lista1+=[554,566,222]
print(lista1)

###
# EJERCICOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]