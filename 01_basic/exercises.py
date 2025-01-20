###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")


### Completa aquí
print("Mi nombre es Gonzalo")
print("Mi ciudad es Misiones")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
print( int("12345"))
print( float("12345"))

print( int(3.99))
print("lo que sucede es que elimina los decimales posterior al entero y no es para redondear el numero hacia el valor 4")

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
nombre,edad,altura=input("como te llamas, que edad tienes y que altura tienes?").split()
print(f"Hola tu nombre es: {nombre}, tienes {edad}, y tienes un altura de {altura}")


print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

pi=3.1416
print(f"el valor de PI: {pi}")

pi_redondeada=round(pi)
print(f"el valor de PI redondeada es {pi_redondeada}")

resultado = pi_redondeada//2
print(f" el valor de PI redondeada dividido 2 es {resultado}")

