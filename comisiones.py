#comisiones del 13%
#el programa debe preguntar el nombre, ventas, el programa tiene que responder "ok, NOMBRE, ganaste XXX
#multiplicar el numero por 13/100
#no más de dos decimales
#dar formato con un string

nombre = input("¿Cómo es tu nombre? ")
ventas = int(input("¿Cuánto has vendido? "))
comisiones = round(ventas * 13 / 100 , 2)
print(f"Hola {nombre}, tus comisiones de este mes son {comisiones} euros")