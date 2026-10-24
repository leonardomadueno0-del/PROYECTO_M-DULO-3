
# PROYECTO DE CONTROL DE INVENTARIO
print("BIENVENIDO AL CONTROL DE INVENTARIO.")
mayor = 0
producto_caro = ""
total_productos = 0

while True:
    try:
        nombre = input("Ingrese el nombre del producto (o 'salir' para terminar): ")

        # Terminar si el usuario escribe salir
        if nombre == "salir":
            break

        cantidad = int(input("Ingrese la cantidad: "))
        costo = float(input("Ingrese el costo del producto: $"))

        # Identificar el producto más caro
        if costo > mayor:
            mayor = costo
            producto_caro = nombre

        total_productos += 1

        print("Se guardó correctamente.")
        print(f"Producto: {nombre} | Cantidad: {cantidad} | Costo: ${costo:.2f}")

    except ValueError:
        print("Ingrese un número válido.")

# Mostrar el resumen final
print(f"Total de productos registrados: {total_productos}")

if total_productos > 0:
    print(f"El producto más caro fue: {producto_caro}")
    print(f"Su precio fue: ${mayor:.2f}")
elif total_productos == 0:
    print("No se registraron productos.")
else:
    print("Error al generar el resumen.")

else:
    print("No se registraron productos.")

