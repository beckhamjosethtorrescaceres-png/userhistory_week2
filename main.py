from aggproduct import agg
from statistics import calculate_statistics

inventory = [] #creacion de lista vacia para almacenar los productos
# Función para mostrar el menú principal
def show_menu(inventory):
    print("\n" + "═" * 60)
    print("       INVENTORY LIST MANAGEMENT - MAIN MENU")
    print("═" * 60)
    print("  1  →  Add product")
    print("  2  →  Show inventory")
    print("  3  →  Calculate statistics")
    print("  4  →  Go out")
    print("═" * 60)

    # Programa principal
    print("╔══════════════════════════════════════╗")
    print("║     WELCOME TO THE INVENTORY         ║")
    print("╚══════════════════════════════════════╝\n")
op = True
while op:
        show_menu(inventory)
        try:
            option = int(input("  → Your choice: "))
            print() # línea en blanco para mejor lectura
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting...")
            continue
        except ValueError: #manejo de error si el usuario ingresa algo que no es un número
            print("  Error! You must enter a number (1-4).\n")
            continue
        except EOFError:
            print("\n\nProgram interrupted by user. Exiting...")
            continue


        if option == 1: #agregar producto
            print("  → Adding product... ")
            product_info = agg()#llamar a la función agg() para obtener la información del producto
            inventory.append(product_info)#agregar el producto al inventario
        elif option == 2: #mostrar inventario
            print("  → Showing inventory... ")
            for product in inventory: #recorrer la lista de productos y mostrar su información
                print(f"  - {product['name']}: ${product['price']:.2f} (quantity: {product['quantity']})")

        elif option == 3: #calcular estadísticas
            print("  → Calculating statistics... ")
            calculate_statistics(inventory)

        elif option == 4:
            print("  ╔════════════════════════════════════════════╗")
            print("  ║   ¡Thank you for using our INVENTORY!      ║")
            print("  ║          ¡Come back soon! 👋               ║")
            print("  ╚════════════════════════════════════════════╝\n")
            break
        else:#manejo de error si el usuario ingresa un número que no corresponde a ninguna opción
            print("  Opción no válida. Elige entre 1 y 4.\n")