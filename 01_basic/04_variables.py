 ###
#04 - variables()
# LAS VARIABLES SIRVEN PARA GUARDART DATOS EN MEMORIA.
#Python es un lenguaje tipado dinamico y de tipado fuerte
###

#Asignar una variable
#solo hace falta poner esto

my_name = "gondev"
print(my_name)

age = 32
print(age)
age=49
print(age)

# Tipado dinamico: el tipo de dato se determina en tiempo de ejecucion.
#no tienes q declararlo explicitamente

name= "dev"
print(type(name))
name=4444
print(type(name))


#tipado fierte: python no realiza conversiones de tipo automatico

# print(10 + "2")
# f-string ( literal de cadena de formato)
print(f"hola {my_name}, tengo {age + 6} años")


#no recomendada forma de asignar variables
name, age, city = "midu", 32, "Bogota"
#no recomiendan


#convenciones de nombre de variables, siemrpe con SNAKE CASE
mi_nombre_de_variable="ok"


#no recomendable para variable es PASCAL CASE
MiNombreDeVariable ="ko"
ninombredevariable="ko"

MI_CONSTANTE = 3.14 #UPPERCASE  para constantes aunque se puede cambiar

#no se puede hacer variales q arranque con numeros, espacios,ni guion para separar, ni palabras reservadas como TRUE/false


