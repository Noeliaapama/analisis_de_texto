from random import randint

nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}, he pensado un número entre el 1 y 100.\nTienes solo 8 intentos para adivinar el número.¡Que te diviertas!")
num_secreto = randint(1,100)

total_intentos = 8
intentos = 0

while intentos < total_intentos:
    numero = int(input("Elige un número entre 1 y 100: "))

    intentos += 1

    if numero < 1 or numero > 100:
        print(f"Ingresa un número válido. Llevas {intentos} intentos")
    elif numero < num_secreto:
        print(f"Tu número es menor al número secreto. Llevas {intentos} intentos")
    elif numero > num_secreto:
        print(f"Tu número es mayor al número secreto. Llevas {intentos} intentos")
    elif numero == num_secreto:
        print(f"¡Enhorabuena {nombre}! Has adivinado en {intentos} intentos")
        break
else:
    print(f"Lo siento {nombre}, has agotado los 8 intentos. El número secreto era {num_secreto}")


