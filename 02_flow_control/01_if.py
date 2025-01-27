 ###
#01 - Sentencias condicionales (if, elif, else)
# permiten ejecutar bloques de codigo solo si se cumplen ciertas condiciones
###

### IMPLIMENTAR BIBLIOTECA PARA ELIMINAR CONSOLA 

import os 
os.system("clear")

print("\n sentenscia simple condicional IF")

edad=18

if edad >= 18:
    print("eres mayor de edad")


print("\n Sentencia condicional con else")

edad =15 
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")  


print("\n Sentencia condicional con Elif")

nota = 7 
if nota >= 9:
    print("Sobresaliente")
elif nota >=7:
    print("Notable!")      
elif nota >=5:
    print("Aprobado!")    
else:
    print("Desaprobado!")            



print("\n condiciones multiples")
edad=25
tiene_carnet= True

if edad >=18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("POLICIAAAA!!!")    



# && -> and
# || -> or
# ! -> if not

#eres de un pueblito y hay cosas locas 

if edad >=18 or tiene_carnet:
    print("puedes conducir en el pueblito")
else: 
    print("paga al policia para q te deje conducir!!")    


es_fin_de_semana= False
if not es_fin_de_semana:
    print("vengaaaa a trabaaajar!")


print("\n anidar condicionales")

edad =20
tiene_dinero = True
if edad >=18:
    if tiene_dinero:
        print("puedes ir a la discoteca")
    else:
        print("quedate en casa")
else:
    print("no puedes entrar a la disco")            


#como simplifar lo de arriba
# 

edad =20
tiene_dinero = True
if edad >=18:
    print("no puedes entrara  la disco")
elif tiene_dinero:
        print("puedes entrar a la disco")
else:
    print("quedate en casa")          





print("\n La condición ternaria:") 
#es una forma concisa de un if-else en una line ade codigo
# [codigo si cumple la condicion] if [la condicion] else [codigo si no cumple]
edad = 17

mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje) 


###
# EJERCICOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales



print("-------------------------EJERCICIOS----------------------------------")
# print("\ndeterminar cual es mayor o si son iguales")
# numero1=input("ingresa el primer numero\n")
# numero2=input("ingresa el segundo numero\n")

# if numero1 < numero2:
#     print(f"el primer numero {numero1} es menor que el segundo numero {numero2}")
# elif numero1 == numero2:
#         print(f"el primer numero {numero1} es igual que el segundo numero {numero2}")
# else:
#     print(f"el primer numero {numero1} es mayor que el segundo numero {numero2}")
    

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)



# print("CALCULADORA, ingresa los dos numeros y el signo de la operacion\n")
# numero1=int(input("ingresa el primer valor\n"))
# numero2=int(input("ingresa el segundo valor\n"))
# operacion=input("ingresa el simbolo de la operacion siendo estos +,-,*,/ \n")

# if operacion == "+":
#     print(f"la suma de {numero1} + {numero2} es igual a: ", numero1+numero2)
# elif operacion == "-":
#     print(f"la resta de {numero1} - {numero2} es igual a: ", numero1-numero2)
# elif operacion == "*":
#     print(f"la multi de {numero1} por {numero2} es igual a: ", numero1*numero2)  
# else:
#     print(f"la div de {numero1} / {numero2} es igual a: ", numero1/numero2)      




# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.


# print("determinemos si es bisiento un año")
# anio=int(input("introduce un año que calculemos\n"))
# if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
#     print(f"{anio} es un año bisiesto.")
# else:
#     print(f"{anio} no es un año bisiesto.")



# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)


# print("dime tu edad y te dire en que categoria estas")
# edad=int(input("que edad tienes?\n"))

# if edad >0 and edad<2:
#     print("eres un Bebé!")
# elif edad >3 and edad<12:
#     print("eres un Niño!")
# elif edad >13 and edad<17:
#     print("eres un Adolescente!")
# elif edad >18 and edad<64:
#     print("eres un Adulto!")            
# else:
#     print("eres Adulto mayor")   