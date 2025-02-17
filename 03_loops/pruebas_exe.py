
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