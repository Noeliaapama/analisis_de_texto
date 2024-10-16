'''def cantidad_tributos(**kwargs):
    return len(kwargs)


resultado = cantidad_tributos(nombre="Noe", ciudad="Jaen", pais="España")
print(resultado)
'''
from random import choices

'''def lista_atributos(**kwargs):
    return list(kwargs.values())
resultado = lista_atributos(edad = 25, profesion = "programador")
print(resultado)'''


'''def describir_persona(nombre, **kwargs):
    descripcion = f"características de {nombre.lower()}:\n"

    descripcion += "\n".join([f"{atributo}: {valor}" for atributo, valor in kwargs.items()])

    print(descripcion)'''

''' EJERCICIO 1
def devolver_distintos(num1,num2,num3):
    suma = num1 + num2 + num3
    if suma > 15:
        return max(num1, num2, num3)
    elif suma < 10:
        return min(num1, num2, num3)
    else:
        numeros = [num1, num2, num3]
        numeros.sort()
        return numeros[1]
print(devolver_distintos(2, 5, 7))  # Devuelve 5 (número intermedio, suma = 14)
print(devolver_distintos(4, 5, 8))  # Devuelve 8 (número mayor, suma = 17)
print(devolver_distintos(1, 2, 3))  # Devuelve 1 (número menor, suma = 6)'''

'''EJERCICIO 2
def letras_separadas(palabra):
    letras = sorted(set(palabra))
    return letras
resultado = letras_separadas("python")
print(resultado)

forma alternativa:
def letras_unicas(palabra):
    mi_set = set ()
    for letra in palabra:
        mi_set.add(letra)
    mi_lista = list(mi_set)
    mi_lista.sort()
    return mi_lista
print("cascarrabias")
'''

''' EJERCICIO 3
def argumentos_indefinidos(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False
print(argumentos_indefinidos(5, 6, 1, 0, 0, 9, 3, 5))  # True
print(argumentos_indefinidos(6, 0, 5, 1, 0, 3, 0, 1))  # False

FORMA ALTERNATIVA:
def cero_vecinos(*args):
    contador = 0
    for num in args:
        if args[contador] == 0 and args[contador + 1] == 0
            return True
        else:
            contador += 1
    return False
print(cero_vecinos(1,2,3,4,5,7,8,9,0,0)) este seria True
print(cero_vecinos(1,2,3,4,5,6,7,8,9,0)) este seria False
'''

def contar_primos():


    choices
    funciones para pedir letra, validar letra y ver si gano



    



