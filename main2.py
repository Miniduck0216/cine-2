def guardar_clientes(clientes):
    with open('clientes.txt', 'w') as file:
        for cliente in clientes:
            file.write(f"{cliente[0]},{cliente[1]}\n")

def guardar_reservas(reserva):
    with open('reservas.txt', 'w') as file:
        for r in reserva:
            file.write(f"{r[0]},{r[1]},{r[2]},{r[3]}\n")

def cargar_clientes():
    try:
        with open('clientes.txt', 'r') as file:
            clientes = []
            for line in file:
                nombre, dni = line.strip().split(',')
                clientes.append([nombre, dni])
            return clientes
    except FileNotFoundError:
        return [["", ""]] * 5

def cargar_reservas():
    try:
        with open('reservas.txt', 'r') as file:
            reserva = []
            for line in file:
                cliente_id, pelicula_id, cantidad, tipo_boleto = map(int, line.strip().split(','))
                reserva.append([cliente_id, pelicula_id, cantidad, tipo_boleto])
            return reserva
    except FileNotFoundError:
        return [[-1, -1, -1, -1]] * 10

def ingresar_cliente(clientes):
    for i in range(len(clientes)):
        if clientes[i][0] == "":
            nombre = input("Ingrese nombre del nuevo cliente: ")
            dni = input("Ingrese cedula del nuevo cliente: ")
            clientes[i] = [nombre, dni]
            guardar_clientes(clientes)  # Guardar clientes actualizados en el archivo
            break
    imprimir_clientes(clientes)

def imprimir_clientes(clientes):
    for cliente in clientes:
        print(f"{cliente[0]}\t\t{cliente[1]}")

def listar_peliculas(peliculas):
    for pelicula in peliculas:
        print(f"ID: {pelicula[0]}, Nombre: {pelicula[1]}, Hora: {pelicula[2]}, Género: {pelicula[3]}")

def buscar_por_nombre(peliculas):
    nombre = input("Ingrese el nombre de la película: ")
    for pelicula in peliculas:
        if nombre.lower() in pelicula[1].lower():
            print(f"ID: {pelicula[0]}, Nombre: {pelicula[1]}, Hora: {pelicula[2]}, Género: {pelicula[3]}")

def buscar_por_genero(peliculas):
    genero = input("Ingrese el género de la película: ")
    for pelicula in peliculas:
        if genero.lower() in pelicula[3].lower():
            print(f"ID: {pelicula[0]}, Nombre: {pelicula[1]}, Hora: {pelicula[2]}, Género: {pelicula[3]}")

def comprar_ticket(peliculas, precio, clientes, reserva):
    cliente_id = int(input("Ingrese el ID del cliente: ")) - 1
    pelicula_id = int(input("Ingrese el ID de la película: ")) - 1
    cantidad = int(input("Ingrese la cantidad de boletos: "))
    
    tipo_boleto = int(input("Ingrese el tipo de boleto (0: General, 1: Estudiante, 2: Niño): "))
    total = precio[tipo_boleto] * cantidad
    
    for i in range(len(reserva)):
        if reserva[i][0] == -1:
            reserva[i] = [cliente_id, pelicula_id, cantidad, tipo_boleto]
            guardar_reservas(reserva)  # Guardar reservas actualizadas en el archivo
            break
    
    print(f"Total a pagar: ${total:.2f}")

def imprimir_factura(cliente, pelicula, cantidad, tipo_boleto, total):
    tipo_boleto_str = ["General", "Estudiante", "Niño"]
    print("\nFactura:")
    print(f"Cliente: {cliente[0]}")
    print(f"Cedula: {cliente[1]}")
    print(f"Película: {pelicula[1]}")
    print(f"Hora: {pelicula[2]}")
    print(f"Género: {pelicula[3]}")
    print(f"Tipo de boleto: {tipo_boleto_str[tipo_boleto]}")
    print(f"Cantidad: {cantidad}")
    print(f"Total a pagar: ${total:.2f}\n")

def imprimir_factura_por_id(peliculas, precio, clientes, reserva):
    reserva_id = int(input("Ingrese el ID de la reserva: "))
    if reserva_id < len(reserva) and reserva[reserva_id][0] != -1:
        r = reserva[reserva_id]
        cliente = clientes[r[0]]
        pelicula = peliculas[r[1]]
        total = precio[r[3]] * r[2]
        imprimir_factura(cliente, pelicula, r[2], r[3], total)
    else:
        print("Reserva no encontrada.")

# Datos iniciales
peliculas = [["1", "Avatar", "10:20", "Fantasia"],
             ["2", "REC", "8:30", "Terror"],
             ["3", "Angry Birds", "11:00", "Animacion"],
             ["4", "Elementos", "12:30", "Animacion"],
             ["5", "Sherk", "9:30", "Fantasia"],
             ["6", "IT", "13:00", "Terror"],
             ["7", "El Aro", "14:30", "Terror"],
             ["8", "Garfield", "15:00", "Animacion"],
             ["9", "Las 50 sombras de grey", "16:00", "Fantasia"],
             ["10", "Sing", "17:30", "Animacion"]]

precio = [7, 3.5, 3]

clientes = cargar_clientes()
reserva = cargar_reservas()

while True:
    print("Escoja una opción:\n1. Ingresar Cliente\n2. Ver Películas\n3. Buscar Película\n4. Comprar Ticket\n5. Imprimir Factura")
    opcion2 = int(input(">> "))

    if opcion2 == 1:
        ingresar_cliente(clientes)
    elif opcion2 == 2:
        listar_peliculas(peliculas)
    elif opcion2 == 3:
        print("1. Por nombre\n2. Por Género")
        opcion3 = int(input(">> "))
        if opcion3 == 1:
            buscar_por_nombre(peliculas)
        elif opcion3 == 2:
            buscar_por_genero(peliculas)
    elif opcion2 == 4:
        comprar_ticket(peliculas, precio, clientes, reserva)
    elif opcion2 == 5:
        imprimir_factura_por_id(peliculas, precio, clientes, reserva)
    
    opcion1 = int(input("¿Desea escoger una nueva opción? 1. Sí / 2. No\n>> "))
    if opcion1 != 1:
      break