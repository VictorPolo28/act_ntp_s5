"""En una sala de videojuegos, se organiza un torneo donde varios jugadores compiten para obtener la mayor cantidad de puntos. Se desea crear un programa en Python que:

Permita ingresar el nombre y puntaje (0 a 10000) de varios jugadores.

Clasifique a cada jugador en un rango gamer según su puntaje:

9000 o más → Leyenda

7000 a 8999 → Pro Gamer

5000 a 6999 → Avanzado

3000 a 4999 → Casual

Menos de 3000 → Novato

Determine si el jugador es Ganador (puntaje ≥ 5000) o Perdedor (puntaje < 5000).

Guarde todos los datos en un diccionario anidado, donde cada clave sea el nombre del jugador y su valor un subdiccionario con:

puntaje

rango

estado (Ganador/Perdedor)

Al finalizar la entrada de datos, el programa debe mostrar:

Lista completa de jugadores con sus datos.

Promedio general de puntajes.

Cantidad de ganadores y perdedores."""


def clasificar_rango(puntaje):
    if puntaje >= 9000:
        return "Leyenda"
    elif puntaje >= 7000:
        return "Pro Gamer"
    elif puntaje >= 5000:
        return "Avanzado"
    elif puntaje >= 3000:
        return "Casual"
    else:
        return "Novato"

jugadores = {}


while True:
    nombre = input("Ingrese el nombre del jugador (o escriba '1' para salir): ").strip()
    if nombre == "1":
        break
    
    try:
        puntaje = int(input(f"Ingrese el puntaje del jugador {nombre}: "))
        
        if puntaje < 0 or puntaje > 10000:
            print("El puntaje debe estar entre 0 y 10000. Intente de nuevo.")
            continue
    except ValueError:
        print("El puntaje debe ser un número.")
        continue
    
    rango = clasificar_rango(puntaje)
    estado = "Ganador" if puntaje >= 5000 else "Perdedor"
    
    
    jugadores[nombre] = {
        "puntaje": puntaje,
        "rango": rango,
        "estado": estado
    }

print("\nResultados Finales ")
suma_puntajes = 0
ganadores = 0
perdedores = 0

for nombre, datos in jugadores.items():
    print(f"{nombre} - Puntaje: {datos['puntaje']} ({datos['rango']}) - {datos['estado']}")
    suma_puntajes += datos["puntaje"]
    if datos["estado"] == "Ganador":
        ganadores += 1
    else:
        perdedores += 1

total_jugadores = len(jugadores)
if total_jugadores > 0:
    promedio = suma_puntajes / total_jugadores
    print(f"\nPromedio de puntaje: {promedio:.2f}")
    print(f"Total de jugadores: {total_jugadores}")
    print(f"Ganadores: {ganadores}")
    print(f"Perdedores: {perdedores}")
else:
    print("No se ingresaron jugadores.")
