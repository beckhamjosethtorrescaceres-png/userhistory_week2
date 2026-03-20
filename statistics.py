def calcular_estadisticas(inventario):
    len_inventario = len(inventario)#obtener la cantidad de productos en el inventario
    
    if len_inventario == 0:#manejo de error si el inventario está vacío
        
        print("  No hay productos en el inventario para calcular estadísticas.\n")
        return#salir de la función si no hay productos en el inventario
    
    else:#calcular estadísticas si hay productos en el inventario
        
        precios = [producto['precio'] for producto in inventario]#crear una lista de precios a partir del inventario
        
        cantidades = [producto['cantidad'] for producto in inventario]
        
        precio_total = sum(precios)#calcular el precio total sumando todos los precios de los productos en el inventario
        cantidad_total = sum(cantidades)
        
        #calcular el valor total del inventario multiplicando el precio por la cantidad de cada producto y sumando los resultados
        valor_total_inventario = sum(producto['precio'] * producto['cantidad'] for producto in inventario)

        print(f"  → Cantidad total de productos: {cantidad_total}")
        print(f"  → Valor total del inventario: ${valor_total_inventario:.2f}\n")
