class Bebida:
    def __init__(self, id, nombre, clasificacion, marca, precio):
        self.id = id
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.marca = marca
        self.precio = precio

bebidas = []

def agregar_bebida():
    id = input("Ingrese el ID de la bebida: ")
    nombre = input("Ingrese el nombre de la bebida: ")
    clasificacion = input("Ingrese la clasificación de la bebida: ")
    marca = input("Ingrese la marca de la bebida: ")
    precio = float(input("Ingrese el precio de la bebida: "))

    bebida = Bebida(id, nombre, clasificacion, marca, precio)
    bebidas.append(bebida)
    print("Bebida agregada correctamente.")

def eliminar_bebida():
    id = input("Ingrese el ID de la bebida que quieres eliminar: ")
    bebida_encontrada = None
    for bebida in bebidas:
        if bebida.id == id:
            bebida_encontrada = bebida
            break

    if bebida_encontrada:
        bebidas.remove(bebida_encontrada)
        print("Bebida eliminada correctamente.")
    else:
        print("No se encontró la bebida con el ID proporcionado.")

def actualizar_bebida():
    id = input("Ingrese el ID de la bebida a actualizar: ")
    bebida_encontrada = None
    for bebida in bebidas:
        if bebida.id == id:
            bebida_encontrada = bebida
            break

    if bebida_encontrada:
        print("Ingrese los nuevos datos de la bebida:")
        nombre = input("Nombre: ")
        clasificacion = input("Clasificación: ")
        marca = input("Marca: ")
        precio = float(input("Precio: "))

        bebida_encontrada.nombre = nombre
        bebida_encontrada.clasificacion = clasificacion
        bebida_encontrada.marca = marca
        bebida_encontrada.precio = precio

        print("Bebida actualizada correctamente.")
    else:
        print("No se encontró la bebida con el ID proporcionado.")

def mostrar_bebidas():
    if not bebidas:
        print("No hay bebidas registradas.")
    else:
        for bebida in bebidas:
            print(f"ID: {bebida.id}")
            print(f"Nombre: {bebida.nombre}")
            print(f"Clasificación: {bebida.clasificacion}")
            print(f"Marca: {bebida.marca}")
            print(f"Precio: {bebida.precio}")

def calcular_precio_promedio():
    if not bebidas:
        print("No hay bebidas registradas.")
    else:
        total = sum(bebida.precio for bebida in bebidas)
        promedio = total / len(bebidas)
        print(f"Precio promedio de las bebidas: {promedio}")

def cantidad_bebidas_marca():
    marca = input("Ingrese el nombre de la marca: ")
    cantidad = sum(1 for bebida in bebidas if bebida.marca == marca)
    print(f"Cantidad de bebidas de la marca {marca}: {cantidad}")

def cantidad_bebidas_clasificacion():
    clasificacion = input("Ingrese la clasificación: ")
    cantidad = sum(1 for bebida in bebidas if bebida.clasificacion == clasificacion)
    print(f"Cantidad de bebidas de la clasificación {clasificacion}: {cantidad}")

def mostrar_menu():
    print("**** Almacén de Bebidas ****")
    print("1. Agregar bebida")
    print("2. Eliminar bebida")
    print("3. Actualizar bebida")
    print("4. Mostrar todas las bebidas")
    print("5. Calcular precio promedio de bebidas")
    print("6. Cantidad de bebidas de una marca")
    print("7. Cantidad de bebidas por clasificación")
    print("8. Salir")

mostrar_menu()

while True:
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregar_bebida()
    elif opcion == "2":
        eliminar_bebida()
    elif opcion == "3":
        actualizar_bebida()
    elif opcion == "4":
        mostrar_bebidas()
    elif opcion == "5":
        calcular_precio_promedio()
    elif opcion == "6":
        cantidad_bebidas_marca()
    elif opcion == "7":
        cantidad_bebidas_clasificacion()
    elif opcion == "8":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

    print()
    mostrar_menu()
