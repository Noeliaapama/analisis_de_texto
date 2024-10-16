import random

# Función que lanza una moneda y devuelve "Cara" o "Cruz"
def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])

# Función que evalúa el resultado de la moneda y actúa sobre una lista de números
def probar_suerte(resultado_moneda, lista_numeros):
    if resultado_moneda == "Cara":
        print("La lista se autodestruirá")
        return []  # Devuelve la lista vacía
    else:
        print("La lista fue salvada")
        return lista_numeros  # Devuelve la lista intacta

# Creamos la lista de números
lista_numeros = [1, 2, 3, 4, 5, 6]

# Llamamos a la función lanzar_moneda para obtener el resultado
resultado = lanzar_moneda()

# Llamamos a la función probar_suerte pasando el resultado y la lista de números
lista_final = probar_suerte(resultado, lista_numeros)

# Imprimimos la lista final
print("Resultado final de la lista:", lista_final)
