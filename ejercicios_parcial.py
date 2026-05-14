'''
Julieta Ponti:
Les dejo dos ejercicios 

1- Los profes de Pensamiento Computacional han lanzado un exitoso emprendimiento de alfajores artesanales. Debido al aumento de las ventas, necesitan gestionar el envío de sus cajas de alfajores a todo el país y desean simular los costos de envíos. El costo de envío de cada paquete se calcula sumando el peso (en gramos) del paquete y un costo fijo que varía según el peso del paquete. Las reglas para modificar el costo fijo son las siguientes:

Si el peso del paquete es menor a 1000 g, el costo fijo se reduce a la mitad.
Si el peso del paquete es mayor o igual a 1000 g y menor o igual a 2000 g, el costo fijo se mantiene sin cambios.
Si el peso del paquete es mayor a 2000 g, el costo fijo se duplica.

Para lograr esto, hacer una función que reciba el valor del costo fijo. La función debe permitir al usuario ingresar el peso de cada paquete, mostrar el costo de envío correspondiente para ese peso, y continuar pidiendo pesos hasta que se ingrese "X" o "x" para salir. 

Al finalizar el ingreso de los pesos, la función debe devolver una lista de tuplas, donde cada tupla contiene dos valores numéricos: el peso ingresado y el costo de envío calculado para ese peso. Por ejemplo, si se recibe un costo fijo de 200 :

>Ingrese el peso (en g) del paquete o 'X' para salir: 300
El costo del envío es 400.0
>Ingrese el peso (en g) del paquete o 'X' para salir: 1300
El costo del envío es 1500.0
>Ingrese el peso (en g) del paquete o 'X' para salir: 3100
El costo del envío es 3500.0
>Ingrese el peso (en g) del paquete o 'X' para salir: x


Se devuelve [(400.0, 300.0), (1500.0, 1300.0), (3500.0, 3100.0)]


2- Una empresa de seguridad aeroportuaria, responsable del control de equipajes en el Aeropuerto Internacional de Ezeiza, dispone de un sistema de rayos X inteligente capaz de identificar, en cada equipaje de mano, todos los envases que contienen líquidos. Dicha máquina devuelve, para cada pieza de equipaje analizada, un listado de pares (“nombre del producto”, volumen en mililitros), por ejemplo:

[("shampoo", 100), ("acondicionador", 112), ("crema de peinar", 90), ("gel", 85), ("perfume", 70)]

Según la normativa vigente, ningún pasajero puede transportar en cabina envases de líquido que superen los 100 ml.
A su vez, existe un limite de 3 envases con líquido. Es decir que no se puede tener más de 3 envases con líquido (que no deben superar el máximo).

Esta empresa nos ha contratado para que desarrollemos una función que, dado el listado de productos detectados por el escáner, determine y devuelva dos listas: una con el nombre de los productos habilitados para el viaje, y otra con el nombre de los productos que deben sacarse del equipaje, de modo que el operador de seguridad pueda informar al pasajero qué modificaciones hacer antes de continuar con el control.

En nuestro caso, si recibimos [("shampoo", 100), ("acondicionador", 112), ("crema de peinar", 90), ("gel", 85), ("perfume", 70)], la función debería devolver ser: ["shampoo", "crema de peinar", "gel"] (habilitados) y  ["acondicionador", "perfume"] (no habilitados).
'''



# ------------------------------ 1 -------------------------------------------------------------------------------------------------

def gestionar_envio_de_alfajores(costo_fijo):
    # envio = costo fijo + peso
    lista_de_envios = []

    peso = input("> Ingrese el peso (en g) del paquete o 'X' para salir: ")

    while peso.lower() != "x":
        peso = float(peso)

        # Si el peso del paquete es menor a 1000 g, el costo fijo se reduce a la mitad.
        if peso < 1000:
            costo_de_envio = (costo_fijo / 2) + peso
            
        # Si el peso del paquete es mayor o igual a 1000 g y menor o igual a 2000 g, el costo fijo se mantiene sin cambios.
        elif 1000 <= peso <= 2000:
            costo_de_envio = costo_fijo + peso

        # Si el peso del paquete es mayor a 2000 g, el costo fijo se duplica.
        else:
            costo_de_envio = (costo_fijo * 2) + peso

        print(f"El costo del envío es: {costo_de_envio}")
        lista_de_envios.append((costo_de_envio, peso))

        peso = input("> Ingrese el peso (en g) del paquete o 'X' para salir: ")
    
    return lista_de_envios

print(gestionar_envio_de_alfajores(200))


# ------------------------------ 2 -------------------------------------------------------------------------------------------------

def escaner_de_productos(lista_de_productos):
    productos_habilitados = []
    productos_no_habilitados = []

    for producto, mililitros in lista_de_productos:
        # Según la normativa vigente, ningún pasajero puede transportar en cabina envases de líquido que superen los 100 ml.
        # A su vez, existe un limite de 3 envases con líquido. Es decir que no se puede tener más de 3 envases con líquido (que no deben superar el máximo).

        if mililitros > 100:
            productos_no_habilitados.append(producto)

        elif len(productos_habilitados) >= 3:
            productos_no_habilitados.append(producto)

        else:
            productos_habilitados.append(producto)

    return productos_habilitados, productos_no_habilitados

print(escaner_de_productos([("shampoo", 100), ("acondicionador", 112), ("crema de peinar", 90), ("gel", 85), ("perfume", 70)]))



    








    