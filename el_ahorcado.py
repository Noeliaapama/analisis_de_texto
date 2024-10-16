import random
'''
- Elegir una palabra al azar.
- Mostras guiones
- El usuario debe ingresar una letra
- Se debe comprobar si la letra está en la palabra, si no lo está, se debe quitar un intento y pedir otra letra.
Mostrar la lista de letras incorrectas, descontar una vida y mostrar restantes.
- si está en la palabra, mostrarla entre los guiones.
- Cuando la palabra esté completa, avisar de que ganó.
- Se debe informar de cuando perdió también.
- 10 intentos.
'''
# En esta función se controla la palabra que el jugador tiene que adivinar
def palabra_azar():
    palabra = ["perro", "gato", "reloj", "aire", "microfono"]
    palabra_aleatoria = random.choice(palabra)
    return palabra_aleatoria

# Ocultar la palabra secreta y que aparezcan guiones
def guiones(palabra):
    return ["_" for _ in palabra] #lista de guiones

def insertar_letra():
    palabra_oculta = palabra_azar()
    letras_adivinadas = guiones(palabra_oculta)
    vidas = 6
    letras_usadas = []

    print(f"Bienvenido al juego del ahorcado, la palabra que debes adivinar es la siguiente: {letras_adivinadas}")

    while vidas > 0 and "_" in letras_adivinadas:
        letra_jugador = input("Inserta una letra: ").lower()
        if letra_jugador in letras_usadas:
            print(f"Ya has usado la letra {letras_usadas}.")
            continue

        letras_usadas.append(letra_jugador)

        if letra_jugador in palabra_oculta:
            for i, letra in enumerate(palabra_oculta):
                if letra == letra_jugador:
                    letras_adivinadas [i] = letra_jugador
            print(f"¡Bien! La letra {letra_jugador} está en la palabra.")
        else:
            vidas -= 1
            print(f"Letra incorrecta, te quedan {vidas} vidas")

        print(f"Progreso actual: {' '.join(letras_adivinadas)}")

        if "_" not in letras_adivinadas:
            print(f"¡Felicidades! Adivinaste la palabra '{palabra_oculta}'.")
            break
    if vidas == 0:
        print(f"Te has quedado sin vidas. La palabra era '{palabra_oculta}'.")

insertar_letra()



