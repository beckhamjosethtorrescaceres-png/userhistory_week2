from aggproduct import agg
from statistics import calcular_estadisticas

inventario = [] #creacion de lista vacia para almacenar los productos
# Función para mostrar el menú principal
def mostrar_menu(inventario):
    print("\n" + "═" * 60)
    print("       MANEJO DE LISTAS EN EL INVENTARIO - MENÚ PRINCIPAL")
    print("═" * 60)
    print("  1  →  Agregar producto")
    print("  2  →  Mostrar inventario")
    print("  3  →  Calcular estadísticas")
    print("  4  →  Salir")
    print("═" * 60)

    # Programa principal
    print("╔══════════════════════════════════════╗")
    print("║     BIENVENIDO AL INVENTARIO         ║")
    print("╚══════════════════════════════════════╝\n")
op = True
while op:
        mostrar_menu(inventario)
        try:
            opcion = int(input("  → Tu opción: "))
            print()  # línea en blanco para mejor lectura
        except ValueError: #manejo de error si el usuario ingresa algo que no es un número
            print("  ¡Error! Debes ingresar un número (1-5).\n")
            continue

        if opcion == 1: #agregar producto
            print("  → Agregando producto... ")
            producto_info = agg()#llamar a la función agg() para obtener la información del producto
            inventario.append(producto_info)#agregar el producto al inventario
        elif opcion == 2: #mostrar inventario
            print("  → Mostrando inventario... ")
            for producto in inventario: #recorrer la lista de productos y mostrar su información
                print(f"  - {producto['nombre']}: ${producto['precio']:.2f} (Cantidad: {producto['cantidad']})")

        elif opcion == 3: #calcular estadísticas
            print("  → Calculando estadísticas... ")
            calcular_estadisticas(inventario)

        elif opcion == 4:
            print("  ╔════════════════════════════════════════════╗")
            print("  ║   ¡Gracias por usar nuestro INVENTARIO!    ║")
            print("  ║          ¡Vuelve pronto! 👋               ║")
            print("  ╚════════════════════════════════════════════╝\n")
            break
        else:#manejo de error si el usuario ingresa un número que no corresponde a ninguna opción
            print("  Opción no válida. Elige entre 1 y 4.\n")