import os
from tabulate import tabulate


# Creacion lista de productos, se agregan 2 en duro
 # productos = [{"codigo":"pc","nombre":"Computador","precio":"1000","cantidad":"1", "cantidadVendida":"1"},{"codigo":"kb","nombre":"Teclado","precio":"2000","cantidad":"1", "cantidadVendida":"2"}]
productos = [
    {"codigo": "pc", "nombre": "Computadora", "precio": 1000000, "cantidad": 50, "ubicacion": "santiago", "cantidadVendida": 300},
    {"codigo": "tecl", "nombre": "Teclado", "precio": 20000, "cantidad": 100, "ubicacion": "santiago", "cantidadVendida": 150},
    {"codigo": "mou", "nombre": "Ratón", "precio": 10000, "cantidad": 15, "ubicacion": "Valparaiso", "cantidadVendida": 200},
    {"codigo": "imp", "nombre": "Impresora", "precio": 50000, "cantidad": 10, "ubicacion": "Valparaiso", "cantidadVendida": 50},
    {"codigo": "cam", "nombre": "Cámara", "precio": 120000, "cantidad": 20, "ubicacion": "santiago", "cantidadVendida": 100}
]

 # Metodo agregar producto 
def agregar_producto(codigo,nombre,precio,cantidad,ubicacion,cantidadVendida):
    producto = {"codigo":codigo,"nombre":nombre,"precio":precio,"cantidad":cantidad,"ubicacion": ubicacion,"cantidadVendida":cantidadVendida} #creacion diccionario producto
    productos.append(producto)

# Metodo actualizar producto 
def actualizar_producto(codigo, nombre=None, precio=None, cantidad=None, ubicacion=None, cantidadVendida=None):
    for producto in productos:
        if producto['codigo'] == codigo:
            if nombre:
                producto['nombre'] = nombre
            if precio:
                producto['precio'] = precio
            if cantidad is not None:
                producto['cantidad'] = cantidad
            if ubicacion:
                producto['ubicacion'] = ubicacion
            if cantidadVendida:
                producto['cantidadVendida'] = cantidadVendida
            return True
    return False

# Metodo Eliminar
def eliminar_producto(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
            productos.remove(producto)

#metodo buscar producto
def buscar_producto(termino):
    resultado = []
    for producto in productos:
        if termino in producto['codigo'] or termino in producto['nombre']:
            resultado.append(producto)
    return resultado

def buscar_producto_por_codigo(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
            return producto

# metodo motrar , retorna la lista productos
def mostrar_inventario():
    return productos

# Obtengo los productos con un stock menor a 25
def productos_con_stock_bajo():
    return [producto for producto in productos if producto["cantidad"] < 25]

def generar_reporte():
    
    # Total de productos
    total_productos = len(productos)
    
    # Productos más vendidos (ordenados por 'cantidadVendida' de mayor a menor)
    productos_mas_vendidos = sorted(productos, key=lambda x: x["cantidadVendida"], reverse=True)[:3]
    
    # Productos con stock bajo
    stock_bajo = productos_con_stock_bajo()
    
    # Generar el reporte
    reporte = {
        "total_productos": total_productos,
        "productos_mas_vendidos": productos_mas_vendidos,
        "productos_stock_bajo": stock_bajo
    }
    
    return reporte

# Funciones para la interfaz de consola
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("\n--- Sistema de Gestión de Inventario ---")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Eliminar producto")
    print("4. Ver inventario")
    print("5. Buscar producto")
    print("6. Generar reporte")
    print("7. Salir")
    return input("Seleccione una opción: ")

# Clase maestra
def main():
    
    while True:
        limpiar_pantalla()
        opcion = menu()

        if opcion == "1":
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad disponible: "))
            ubicacion = input("Ingrese ubicación: ")
            cantidadVendida = int(input("Ingrese la cantidad Vendida: "))
            agregar_producto(codigo,nombre,precio, cantidad, ubicacion, cantidadVendida)
            print("Producto agregado con éxito.")

        elif opcion == "2":
            codigo = input("Ingrese el código del producto a actualizar: ")
            if buscar_producto_por_codigo(codigo):                 
                nombre = input("Ingrese el nuevo nombre (presione Enter para omitir): ") or None
                precio = input("Ingrese el nuevo precio (presione Enter para omitir): ")
                precio = float(precio) if precio else None
                cantidad = input("Ingrese la nueva cantidad (presione Enter para omitir): ")
                cantidad = int(cantidad) if cantidad else None
                ubicacion = input("Ingrese la nueva ubicación (presione Enter para omitir): ")
                cantidadVendida = int(input("Ingrese la cantidad Vendida (presione Enter para omitir): "))
                if actualizar_producto(codigo, nombre, precio, cantidad, ubicacion,cantidadVendida):
                    print("Producto actualizado con éxito.")
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            codigo = input("Ingrese el código del producto a eliminar: ")
            if buscar_producto_por_codigo(codigo):  
                eliminar_producto(codigo)
                print("Producto eliminado con éxito.")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            
            productos_bajo_stock = [
                f"{producto['nombre']} ({producto['cantidad']})"
                for producto in reporte["productos_stock_bajo"]
            ]

            # Verifica si hay productos con bajo stock
            if productos_bajo_stock:
                print("Productos con bajo stock: ", ", ".join(productos_bajo_stock))

            productos = mostrar_inventario()
            if productos:
                print("\nInventario actual:")
                
                # Preparar datos para la tabla
                encabezados = ["Código", "Nombre", "Precio", "Cantidad", "Ubicación", "Cantidad Vendida"]
                datos = [
                    [producto["codigo"], producto["nombre"], producto["precio"], producto["cantidad"], producto["ubicacion"], producto["cantidadVendida"]]
                    for producto in productos
                ]
                
                # Imprimir la tabla
                print(tabulate(datos, headers=encabezados, tablefmt="grid"))
            else:
                print("El inventario está vacío.")

        elif opcion == "5":
            termino = input("Ingrese el nombre o código del producto a buscar: ")
            resultados = buscar_producto(termino)
            if resultados:
                print("\nResultados de la búsqueda:")
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos.")

        elif opcion == "6":
            reporte = generar_reporte()
            
            # total productos
            print("\nReporte de inventario:")
            print(f"Total de productos: {reporte['total_productos']}")

            # productos mas vendidos
            mas_vedidos = [
                f"{producto['nombre']} ({producto['cantidadVendida']})"
                for producto in reporte["productos_mas_vendidos"]
            ]
            print("Productos más vendidos: " + ", ".join(mas_vedidos))

            # stock bajo
            productos_bajo_stock = [
                f"{producto['nombre']} ({producto['cantidad']})"
                for producto in reporte["productos_stock_bajo"]
            ]
            print("Productos con bajo stock: ", ", ".join(productos_bajo_stock))
            

        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

        input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()
