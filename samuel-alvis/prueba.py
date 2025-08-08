productos = [
    {"nombre": "manzana", "estado": "disponible"},
    {"nombre": "banana", "estado": "vendido"},
    {"nombre": "naranja", "estado": "disponible"},
    {"nombre": "kiwi", "estado": "disponible"},
    {"nombre": "pera", "estado": "vendido"}
]

limite_ventas = 2
ventas_realizadas = 0

while ventas_realizadas < limite_ventas:
    print(f"\n--- Bucle While: Iteración {ventas_realizadas + 1} de {limite_ventas} ---")

    for producto in productos:

        if producto["estado"] == "disponible":
            print(f"El producto '{producto['nombre']}' está disponible. Realizando venta...")

            if ventas_realizadas < limite_ventas:
                producto["estado"] = "vendido"
                ventas_realizadas += 1
                print(f"Venta de '{producto['nombre']}' realizada. Total de ventas: {ventas_realizadas}")

                break
            else:
                break
    
    if ventas_realizadas >= limite_ventas:
        print("\n¡Límite de ventas alcanzado!")
        break


print("\n--- Estado final de los productos ---")
for producto in productos:
    print(f"Producto: {producto['nombre']}, Estado: {producto['estado']}")