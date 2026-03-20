def agg():
    
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    #crear un diccionario con la información del producto
    producto_info = {
        "nombre": producto,
        "precio": precio,
        "cantidad": cantidad
    }
    return producto_info