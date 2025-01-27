###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas
###

import os
os.system("clear")

lista1=[1,2,3,4,5]
lista1.append(6)#añade al final
print(lista1)

lista1.insert(1, 20)#inserta un elemento en la posciion que le indiquemos como primer argumetno
print(lista1)
lista1.extend(['a','b']) #agrega elementos al final
print(lista1)

#eliminar elementos de la lista
lista1.remove('a')#elimina la primera aparicion nomas
print(lista1)

ultimo = lista1.pop()#elimina el ultimo de la lista
print(lista1)
print(ultimo)

lista1.pop(3)#elimina el ultimo de la lista
print(lista1)

del lista1[-1]#eliminar por lo bestia
print(lista1)

lista1.clear() #elimna todos los elementos
print(lista1)

#elimina un rango de elementos
lista1=[55,77,8822,111,3333,77777777,9,1,2,3,4,5,34523,100]
del lista1[1:3]
print(lista1)


#mas metodos utiles
print("ordenar listas")
lista1.sort()#modifica la lista y no la guarda una copia de ella pa eso hay q hacer lo de abajo mas abajo
print(lista1)

#crear la copia
lista11=[55,77,8822,111,3333,77777777,9,1,2,3,4,5,34523,100]
lista_orde= sorted(lista11)
print(lista_orde)



print("Ordenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)


#mas metodos utiles
animals=[99,88,77]
print(len(animals))#que longitud tiene
print(animals.count(77))#cuantas veces aparece
print(77 in animals)#true o false




###
# EJERCICOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

lista55=[1,2,3,4,5]
lista55.append(6)
lista55.insert(1,10)
print(lista55)





# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

lista_a.extend(lista_b)
print(lista_a)
lista_a.remove(1)
print(lista_a)
pop=lista_a.pop(3)
print(pop)
lista_b.clear()






# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

lista34=[1,2,3,4,5,6,7,8,9,10]
del lista34[2:5]
print(lista34)

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

lista65=[5, 2, 8, 1, 9, 4, 2]
lista65.sort()
print(lista65)
print(lista65.count(2))




# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

lista_orig=[1, 2, 3]
copia1= lista_orig[:]
print(copia1)






# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.