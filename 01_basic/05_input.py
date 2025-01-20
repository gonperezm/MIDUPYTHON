 ###
#05 - entrada de usuarios (input()) - version simplificada
# la función input() permite obtener datos del usuario a traves dela consola
###


# nombre= input("Hola, como te llamas?\n")
# print(f"Hola {nombre}, encantado de conocerte")

# age=input("cuantos años tienes?\n")
# age= int(age)
# print(f"tienes {age} años")

print("Obtener multiples valores a la vez")
country, city = input("en que pais y ciudad vives?\n").split()

print(f"vives en {country}, {city}  ")

