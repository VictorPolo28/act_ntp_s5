""" 5 Ejercicios de Condicionales
Número positivo, negativo o cero:
Escribe un programa que pida un número al usuario e imprima si es positivo, negativo o cero.

Mayor de tres números:
Solicita tres números e imprime cuál es el mayor.

Año bisiesto:
Pide al usuario un año e indica si es bisiesto (divisible por 4, excepto múltiplos de 100, salvo que también sean divisibles por 400).

Edad para votar:
Pide la edad del usuario e indica si puede votar (mayor o igual a 18 años).

Par o impar:
Solicita un número e imprime si es par o impar."""

#1 Número positivo, negativo o cero: Escribe un programa que pida un número al usuario e imprima si es positivo, negativo o cero.

numero =int(input("Ingrese un numero  cualquiera"))
if numero < 0 :
    print("El  numero es negativo")

else :
    print("el numero es positivo")


#2 Mayor de tres números: Solicita tres números e imprime cuál es el mayor.
num1 = int(input("ingrese el  primer  numero: "))
num2 = int(input("ingrese  el  segundo numero:"))
num3 = int(input("ingrese  el   tercer numero"))

if num1 > num2  and num1 > num3 :
    print(f"El numero {num1} es mayor que   el nuemro {num2}  y {num3}")

elif num2 > num1  and num2 > num3:
    print(f"El numero {num2} es mayor que   el nuemro {num1}  y {num3}")
else:
    print(f"El numero {num3} es mayor que   el nuemro {num2}  y {num1}")

#3Año bisiesto: Pide al usuario un año e indica si es bisiesto (divisible por 4, excepto múltiplos de 100, salvo que también sean divisibles por 400).

año = int(input("Ingrese   el  año que  desea validar"))

if (año % 4 == 0  and año % 100 != 0)  or (año % 400 == 0):
    print(f"El año {año} es un año  bisiesto")
else:
    print(f"El año {año} no es  bisiesto")

#4 Edad para votar:Pide la edad del usuario e indica si puede votar (mayor o igual a 18 años).

edad = int(input("Ingrese   la edad  del votante: "))
if  edad  < 18 :
    print("El votante no puedeser  menor de edad:")
else: 
    print("El votante tiene la edad requerida  para votar: ")

#5 Par o impar: Solicita un número e imprime si es par o impar."""

numers = int(input("Ingrese un numero positivo "))
if numers <= 0:
    print("El numero no puede   ser engativo  o cero")
elif numers % 2 == 0:
    print("El numero es par")
else:
    print("El numero  es  impar")

