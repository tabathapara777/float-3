import datetime
import json


catalogo_pizzas = {
    "CuatroQuesos": {
        "Pequeña": 6000,
        "Mediana": 9000,
        "Familia": 12000
    },
    "Hawaiana": {
        "Pequeña": 6000,
        "Mediana": 9000,
        "Familia": 12000
    },
    "napolitana": {
        "Pequeña": 5500,
        "Mediana": 8500,
        "Familia": 11000
    },
    "pepperoni": {
        "Pequeña": 7000,
        "Mediana": 10000,
        "Familia": 13000
    }
}

ventas = []

ventas = []

def mostrar_menu():
    print("\nBienvenido al sistema de ventas de pizzas en DUOC UC")
    print("1. Registrar una venta")
    print("2. Mostrar todas las ventas")
    print("3. Buscar ventas por cliente")
    print("4. Guardar las ventas en un archivo")
    print("5. Cargar las ventas desde un archivo")
    print("6. Generar Boleta")
    print("7. Anular Venta")
    print("8. Salir del programa")

def registrar_venta():
    cliente = input("Ingrese el nombre del cliente: ")
    tipo_pizza = input("Ingrese el tipo de pizza (CuatroQuesos, Hawaiana, napolitana,pepperoni): ")
    tamaño = input("Ingrese el tamaño de la pizza (Pequeña, Mediana, Familia): ")

  
    if tipo_pizza in catalogo_pizzas and tamaño in catalogo_pizzas[tipo_pizza]:
        precio = catalogo_pizzas[tipo_pizza][tamaño]
    else:
        print("Tipo de pizza o tamaño no válido.")
        return
    
    tipo_usuario = input("Ingrese el usuario (Estudiante diurno, Estudiante vespertino, Administrativo): ").lower()
    descuento = 0.0

    if tipo_usuario == "estudiante diurno":
        descuento = 0.12
    elif tipo_usuario == "estudiante vespertino":
        descuento = 0.14
    elif tipo_usuario == "administrativo":
        descuento = 0.10
    else:
        print("Tipo de usuario no válido.")
        return
    
    total_descuento = precio * descuento
    precio_final = precio - total_descuento

    venta = {
        "cliente": cliente,
        "tipo_pizza": tipo_pizza,
        "tamaño": tamaño,
        "precio_final": precio_final,
        "fecha_hora": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")       
    }

    ventas.append(venta)
    print("Venta registrada satisfactoriamente.")

def mostrar_ventas():
    if ventas:
        for idx, venta in enumerate(ventas, start=1):
            print(f"\nVenta {idx}:")
            print(f"Cliente: {venta['cliente']}")
            print(f"Tipo de pizza: {venta['tipo_pizza']}")
            print(f"Tamaño: {venta['tamaño']}")
            print(f"Precio final: ${venta['precio_final']:.2f}")
            print(f"Fecha y hora: {venta['fecha_hora']}")
    else:
        print("No hay ventas registradas.")

def buscar_por_cliente():
    cliente_buscar = input("Ingrese el nombre del cliente a buscar: ")
    encontradas = [venta for venta in ventas if venta['cliente'].lower() == cliente_buscar.lower()]

    if encontradas:
        print(f"\nVentas encontradas para el cliente '{cliente_buscar}':")
        for idx, venta in enumerate(encontradas, start=1):
            print(f"\nVenta {idx}:")
            print(f"Tipo de pizza: {venta['tipo_pizza']}")
            print(f"Tamaño: {venta['tamaño']}")
            print(f"Precio final: ${venta['precio_final']:.2f}")
            print(f"Fecha y hora: {venta['fecha_hora']}")
    else:
        print(f"No se encontraron ventas para el cliente '{cliente_buscar}'.")

def guardar_en_archivo():
    nombre_archivo = input("Ingrese el nombre del archivo para guardar las ventas (sin extensión): ") + ".json"
    with open(nombre_archivo, 'w') as file:
        json.dump(ventas, file, indent=4)
    print(f"Ventas guardadas en '{nombre_archivo}'.")

def cargar_desde_archivo():
    nombre_archivo = input("Ingrese el nombre del archivo para cargar las ventas (incluyendo la extensión .json): ")
    try:
        with open(nombre_archivo, 'r') as file:
            global ventas
            ventas = json.load(file)
        print(f"Ventas cargadas desde '{nombre_archivo}'.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

def generar_boleta():
    if ventas:
        idx_venta = int(input("Ingrese el número de venta para generar boleta: ")) - 1
        if 0 <= idx_venta < len(ventas):
            venta = ventas[idx_venta]
            print("\n------------------- Boleta de Venta -------------------")
            print(f"Fecha y hora: {venta['fecha_hora']}")
            print(f"Cliente: {venta['cliente']}")
            print(f"Tipo de pizza: {venta['tipo_pizza']}")
            print(f"Tamaño: {venta['tamaño']}")
            print(f"Precio final: ${venta['precio_final']:.2f}")
            print("-------------------------------------------------------")
        else:
            print("Número de venta no válido.")
    else:
        print("No hay ventas registradas.")

def anular_venta():
    print("Compra Anulada Correctamente")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción del menú (1-8): ")

        if opcion == '1':
            registrar_venta()
        elif opcion == '2':
            mostrar_ventas()
        elif opcion == '3':
            buscar_por_cliente()
        elif opcion == '4':
            guardar_en_archivo()
        elif opcion == '5':
            cargar_desde_archivo()
        elif opcion == '6':
            generar_boleta()
        elif opcion == '7':
            anular_venta()
        elif opcion == '8':    
            print("Cerrando la opcion del programa...")
            break
        else:
            print("Opción no válida")