# Creamos dos listas vacías para almacenar números pares e impares
pares = []  # Lista para los números pares
impares = []  # Lista para los números impares

# Mensaje inicial
print("Este programa te permite ingresar numeros y los clasifica como pares o impares.")

# Iniciamos un bucle while para pedir números al usuario
while True:
    # Pedimos al usuario que ingrese un número
    numero = input("Ingresa un numero (o escribe 'salir' para terminar): ")
    
    # Comprobamos si el usuario quiere salir
    if numero.lower() == 'salir':
        break  # Si el usuario escribe 'salir', terminamos el bucle
    
    # Intentamos convertir el número ingresado a entero
    try:
        numero = int(numero)  # Convertimos la entrada a entero
    except ValueError:  # Si no es posible convertirlo, le mostramos un error
        print("Eso no es un numero valido, intenta de nuevo.")
        continue  # Volvemos a pedir el número si la conversión falla
    
    # Usamos un condicional para verificar si el número es par o impar
    if numero % 2 == 0:
        pares.append(numero)  # Si es par, lo agregamos a la lista 'pares'
    else:
        impares.append(numero)  # Si es impar, lo agregamos a la lista 'impares'

# Una vez que el bucle termina, mostramos los resultados
print("\nNumeros clasificados:")
print("Pares:", pares)  # Mostramos la lista de números pares
print("Impares:", impares)  # Mostramos la lista de números impares

# Usamos un bucle 'for' para iterar sobre la lista de pares y mostrar sus elementos
print("\nNumeros pares:")
for numero in pares:
    print(numero)  # Mostramos cada número par en la lista 'pares'

# Usamos otro bucle 'for' para iterar sobre la lista de impares y mostrar sus elementos
print("\nNumeros impares:")
for numero in impares:
    print(numero)  # Mostramos cada número impar en la lista 'impares'