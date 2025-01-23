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