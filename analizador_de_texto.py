texto = input("Escribe una frase: ")
letras = [] #lista para las letras

texto = texto.lower() #para poner todo en minusculas

letras.append(input("Inserta la primera letra: ").lower()) #append incluye las letras en la lista de letras
letras.append(input("Inserta la segunda letra: ").lower()) #lower controla que todo sea minusculas
letras.append(input("Inserta la tercera letra: ").lower())

print("\n") #salto de linea
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0]) #esto va a contar la cantidad de esa letra en la lista letras
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra {letras[0]} repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra {letras[1]} repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra {letras[2]} repetida {cantidad_letras3} veces")

print("\n") #salto de linea
print("CANTIDAD DE PALABRAS")
palabras = texto.split() #palabras va a ser una lista que va a contener todas las palabras de texto
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = " ".join(palabras)
print(f"Si ordenamos tu texto al revés va a decir: '{texto_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = "python" in texto
dic = {True: "si", False: "no"}
print(f"La palabra 'python' {dic[buscar_python]} se encuentra en el texto")


