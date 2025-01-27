###
# 02_ booleanos
# Valores logicos: True(Verdadero) y False(Falso).
# Fundamentales para el control de flujo y la logica de programacion.
###

import os 
os.system("clear")

print(" Valores booleanos basicos:")
print(True)
print(False)

#operadores de comparacion: devuelven un booleano

print("5 < 3:", 5>3) #True
print("5 > 3:", 5<3) #False
print("5 == 5:", 5==5) #True (igualdad)
print("5 != 3:", 5 !=3) #True ( desigualdad)
print("5 >= 5:", 5>=5) #True (mayor o igual que)
print("5 <= 3:", 5>=3) #False (menor o igual que)


print("comparacion de cadenas:")
print("manzana < pera: ", "manzana"<"pera") #true cuidad q da true porque compara caracter por caracter 
print("'Hola' == 'hola'", 'Hola' == 'hola') #false, porq es sensible los upper cap
 

print("\nTablas de la verdad")
print("and:")
print("A        B       A and B")
print("True   True      ", True and True)
print("True   False     ", True and False)
print("False   True     ", False and True)
print("False   False    ", False and False)


print("\nor:")
print("A        B       A or B")
print("True   True      ", True and True)
print("True   False     ", True and False)
print("False   True     ", False and True)
print("False   False    ", False and False)

print("\nnot:")
print("A        not A")
print("True   ", not True)
print("False  ", not False)