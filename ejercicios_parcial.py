import random
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
'''
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
'''


# ------------------------------ 2 -------------------------------------------------------------------------------------------------
'''
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
'''


# ------------------------------ 3 -------------------------------------------------------------------------------------------------
'''
Ejercicio 3
En una fábrica de alimentos, el encargado de logística cada día debe armar la lista de productos que se van a despachar. Hasta ahora este proceso se hacía a mano en papel y resultaba poco práctico, porque luego había que repartir copias a cada chofer de camión. Para optimizarlo, se decidió digitalizar la generación de la lista diaria.

Cada tipo de producto se identifica con un código alfanumérico de exactamente 4 caracteres. Además, como cada camión solo transporta un tipo de producto, el número de productos diferentes que se pueden despachar en la jornada está limitado por la cantidad de camiones disponibles.

El encargado necesita entonces un programa que, dada una cantidad de camiones, permita:

• Ingresar los códigos de los productos a despachar hasta alcanzar el máximo de camiones, y seguir solicitando códigos mientras no se haya alcanzado ese máximo.
• Rechazar los códigos que no tengan exactamente 4 caracteres.
• Rechazar los códigos repetidos, indicando el error.
• Si el código tiene 4 caracteres y no está repetido, guardarlo.
• Al finalizar, devolver la lista final de productos a despachar en la jornada.

Por ejemplo, si se recibe una cantidad de camiones 3:

Ingrese un código de producto: A34FS
El código debe contener exactamente 4 caracteres
Ingrese un código de producto: A34F
¡Se ha guardado el código!
Ingrese un código de producto: AA33
¡Se ha guardado el código!
Ingrese un código de producto: AA33
El código ya fue ingresado anteriormente
Ingrese un código de producto: AA32
¡Se ha guardado el código!

La función deberá devolver: ["A34F", "AA33", "AA32"]
'''

'''
def productos_a_despachar(cantidad_max_de_camiones):
    listaproductos = []

    while len(listaproductos) < cantidad_max_de_camiones:

        codigoproducto = input("> Ingrese un código de producto: ")

        # Rechazar los códigos que no tengan exactamente 4 caracteres.
        if len(codigoproducto) != 4:
            print("El código debe contener exactamente 4 caracteres")
        
        # Rechazar los códigos repetidos, indicando el error.
        elif codigoproducto in listaproductos:
            print("El código ya fue ingresado anteriormente")
        
        # Si el código tiene 4 caracteres y no está repetido, guardarlo.
        else: 
            listaproductos.append(codigoproducto)
            print("¡Se ha guardado el código!")

    return listaproductos

print(productos_a_despachar(3))
'''


# ------------------------------ 4 -------------------------------------------------------------------------------------------------
'''
Ejercicio 4

Trabajamos en un laboratorio de investigación donde analizamos ADN digital representado como cadenas de símbolos de ceros y unos, donde cada símbolo representa una base artificial, y cada secuencia contiene información genética codificada. Por ejemplo, una secuencia podría ser "11010110110110101010". Como el programa filtra la secuencia de ADN varias veces, también podría pasar que ocurra alguna mutación inesperada y se agreguen símbolos que no sean 0 o 1, como por ejemplo: "1f1010110111V3011010".
Queremos realizar un análisis e investigar la presencia de ciertos patrones dentro de la cadena de ADN artificial. Para ello, necesitamos hacer una función que reciba una cadena y un patrón buscado dentro de la misma y nos devuelva la siguiente información en una estructura no mutable de elementos ordenados:

• Cantidad de 1 presentes en la cadena
• Cantidad de 0 presentes en la cadena
• Cantidad de veces que aparece el patrón dado, dentro de la cadena.
• Posición de la primera aparición del patrón dentro de la cadena (sabemos que siempre aparece al menos una vez).
• Porcentaje de elementos que hay dentro de la secuencia que no son 0 ni 1.

Por ejemplo: si se recibe la secuencia "1f1010110111V3011010" y el patrón "1010", se debe devolver 10, 6, 2, 2 y 15.78.

Hacer una función que cumpla con lo solicitado.
'''

'''
def analizar_adn_digital(cadena, patron):
    # Cantidad de 1 presentes en la cadena
    cantidad_1 = cadena.count("1")
    # Cantidad de 0 presentes en la cadena
    cantidad_0 = cadena.count("0")
    # Cantidad de veces que aparece el patrón dado, dentro de la cadena.
    cantidad_patron = cadena.count(patron)
    # Posición de la primera aparición del patrón dentro de la cadena (sabemos que siempre aparece al menos una vez).
    patron_pos = cadena.find(patron)
    # Porcentaje de elementos que hay dentro de la secuencia que no son 0 ni 1.
    ni_0_ni_1 = 0

    for elemento in cadena:
        if elemento != "0" and elemento != "1":
            ni_0_ni_1 += 1

    porcentaje = (ni_0_ni_1 / len(cadena)) * 100


    return (cantidad_1, cantidad_0, cantidad_patron, patron_pos, round(porcentaje, 2))

print(analizar_adn_digital("1f1010110111W301010", "1010"))
'''


# ------------------------------ 5 -------------------------------------------------------------------------------------------------
'''
Ejercicio 5

Un auto tiene un tanque con cierta cantidad de nafta al inicio del viaje. El viaje se divide en tramos, y cada tramo tiene distancia aleatoria:

• La distancia de cada tramo se genera aleatoriamente entre 10 y 50 km.
• El tiempo de cada tramo es de 1 hora.
• El consumo de nafta de cada tramo depende de la distancia, usando un valor fijo de consumo por kilómetro (0.1 litros/km).

Se debe crear una función que reciba como parámetro la cantidad de nafta al inicio y simule el viaje hasta que la nafta disponible sea menor a un nivel crítico (15 litros). La función debe:

• Mostrar los tramos recorridos indicando la distancia y la nafta restante.
• Detener la simulación cuando la nafta llegue al nivel crítico y mostrar un mensaje de alerta.
• Al final, mostrar un resumen del viaje con: distancia total recorrida, tiempo total empleado, velocidad promedio del viaje (distancia total / tiempo total), nafta restante.

```
# Devuelve un numero aleatorio del 1 al 50
numero = random.randint(1, 50)

# Para calcular el consumo de nafta en un tramo
nafta_consumida = tramo * consumo
```

Ejemplo de ejecución del programa:

```
Iniciando simulación — Nafta inicial: 30 litros
Tramo recorrido: 17 km. Nafta restante: 28.30 litros
Tramo recorrido: 11 km. Nafta restante: 27.20 litros
Tramo recorrido: 42 km. Nafta restante: 23.00 litros
Tramo recorrido: 30 km. Nafta restante: 20.00 litros
Tramo recorrido: 22 km. Nafta restante: 17.80 litros
Tramo recorrido: 14 km. Nafta restante: 16.40 litros
Tramo recorrido: 11 km. Nafta restante: 15.30 litros
Tramo recorrido: 29 km. Nafta restante: 12.40 litros
¡Atención! La nafta está llegando al nivel crítico. Busque una estación de servicio.

=== Resumen del viaje ===
Distancia total recorrida: 176 km
Tiempo total empleado: 8.00 horas
Velocidad promedio: 22.00 km/h
Nafta restante: 12.40 litros
```

Puede ocurrir que el valor de nafta pasado por parámetro sea menor al límite mínimo, si es ese el caso, se debe omitir la simulación y terminar la función imprimiendo un mensaje de error.

```
Error. Nafta insuficiente para la simulación.
```

'''

'''
def viaje_en_auto(nafta):
    if nafta < 15:
        print("Error. Nafta insuficiente para la simulación.")
        return
    
    print(f"Iniciando simulación — Nafta inicial: {nafta} litros")
    distancia_total = 0
    tiempo_total = 0
    while nafta >= 15:
        tramo = random.randint(10, 50)

        distancia_total += tramo

        nafta -= (tramo * 0.1)
        print(f"Tramo recorrido: {tramo} km. Nafta restante: {round(nafta, 2)} litros")
        tiempo_total += 1

        if nafta < 15:
            print("¡Atención! La nafta está llegando al nivel crítico. Busque una estación de servicio.")
            break


    print("=== Resumen del viaje ===")
    print(f"Distancia total recorrida: {distancia_total} km")
    print(f"Tiempo total empleado: {tiempo_total} horas")
    print(f"Velocidad promedio: {round(distancia_total / tiempo_total, 2)} km/h")
    print(f"Nafta restante: {round(nafta, 2)} litros")

viaje_en_auto(30)
'''


# ------------------------------ 6 -------------------------------------------------------------------------------------------------
'''
Ejercicio 6

Spotiti quiere analizar qué usuario es el que más utilizó la plataforma de música durante la semana. Cada usuario se representa con una tupla de la forma:

```
(nombre, horas_escuchadas, género_favorito)
```

Por ejemplo:

```
usuarios = (
    ("Juan", 10, "Rock"),
    ("María", 7, "Pop"),
    ("Carlos", 12, "Clásica"),
    ("Laura", 4, "Rock"),
    ("Sofía", 9, "Pop")
)
```

Se pide crear una función que determine quién es el usuario que escuchó más horas de música y devuelva su nombre y género favorito en una tupla con el siguiente formato:

```
(nombre_del_que_más_escuchó, género_del_que_más_escuchó)
```
'''

'''
usuarios = (
    ("Juan", 10, "Rock"),
    ("María", 7, "Pop"),
    ("Carlos", 12, "Clásica"),
    ("Laura", 4, "Rock"),
    ("Sofía", 9, "Pop")
)

def quien_escucho_mas(usuarios):
    mayor_nombre, mayor_horas, mayor_genero = usuarios[0]

    for nombre, horas, genero in usuarios:
        if horas > mayor_horas:
            mayor_nombre, mayor_horas, mayor_genero = nombre, horas, genero

    return (mayor_nombre, mayor_genero)

print(quien_escucho_mas(usuarios))
'''


# ------------------------------ 7 -------------------------------------------------------------------------------------------------
'''
Ejercicio 7
El departamento de espacios verdes de la ciudad tiene que organizar las cuadrillas de fumigación contra el dengue para la próxima primavera, para lo cual cuenta con una lista de espacios a fumigar, con el nombre y los metros cuadrados y otra con las cuadrillas disponibles, con el código de cuadrilla y la capacidad en metros cuadrados. Más abajo se pueden ver ejemplos de ambas listas. Antes de empezar a organizar, debe saber si es posible abarcar todos los metros cuadrados de los espacios con las cuadrillas disponibles.

a. Desarrollar una función que indique si la suma de todos los espacios puede ser cubierta por el total de las cuadrillas.

b. Desarrollar otra función que devuelva, en una tupla, las 3 cuadrillas con mayor capacidad.

Por ejemplo

# Espacios verdes
espacios_verdes = [("parque centenario",15000),("Parque Chacabuco", 25000),("Plazoleta Pugliese",12),
("Plaza Las Heras",5000)]

#Cuadrillas
cuadrillas = [("C-110001", 35000),("C-110002", 10000),("C-110000",900),("C-110005",70000)]
'''

'''
def puede_ser_cubierta(espacios, cuadrillas):
    total_espacios = 0
    total_cuadrillas = 0

    for plaza, espacioverde in espacios:
        total_espacios += espacioverde

    for cuadrilla, espacio in cuadrillas:
        total_cuadrillas += espacio
    
    return total_espacios <= total_cuadrillas

def espacio_de_cuadrilla(cuad):
        return cuad[1]

def cuadrillas_con_mas_capacidad(cuadrillas):
    cuadrillas = sorted(cuadrillas, key=espacio_de_cuadrilla, reverse=True)

    return tuple(cuadrillas[:3])

print(cuadrillas_con_mas_capacidad([("C-110001", 35000),("C-110002", 10000),("C-110000",900),("C-110005",70000)]))
print(puede_ser_cubierta([("parque centenario",15000),("Parque Chacabuco", 25000),("Plazoleta Pugliese",12), ("Plaza Las Heras",5000)], [("C-110001", 35000),("C-110002", 10000),("C-110000",900),("C-110005",70000)]))
'''

# ------------------------------ 8 -------------------------------------------------------------------------------------------------

'''
Ejercicio 8
Luego de las últimas inundaciones, decidimos recolectar alimentos, vestimenta y cualquier elemento que pueda ser útil para los afectados. Para no tener que contar manualmente, decidimos armar una función que nos ayude:

Armar una función que solicite donaciones al usuario hasta que ingrese "*", sabiendo que las donaciones tendrán el formato "<cantidad>-<elemento>". Al finalizar, debemos imprimir un mensaje indicando que elementos han donado y devolver el total de donaciones.

Ver el siguiente ejemplo:

> Bienvenido! Que desea donar?: "2-agua"
> Gracias por la donación! Qué más desea donar?: "1-arroz"
> Gracias por la donación! Qué más desea donar?: "4-campera"
> Gracias por la donación! Qué más desea donar?: "*"
> Muchas gracias por tu ayuda, has donado: agua - arroz - campera

Debe devolver 7.
'''

'''
def donar_al_usuario():
    donaciones = []
    total_donado = 0
    donacion = input("> Bienvenido! Que desea donar?: ")
    
    while donacion != "*":
        donacion = donacion.split("-")
        donaciones.append(donacion[1])
        total_donado += int(donacion[0])

        donacion = input("> Gracias por la donación! Qué más desea donar?: ")
    
    print(f"> Muchas gracias por tu ayuda, has donado: {' - '.join(donaciones)}")

    return total_donado

print(donar_al_usuario())
'''

# ------------------------------ 9 -------------------------------------------------------------------------------------------------
'''
Ejercicio 9

Para la nueva temporada del reality Gran Hermano, la producción busca modernizar el sistema de puntuación de los participantes. Como saben que estás cursando Pensamiento Computacional, te eligieron para colaborar en esta tarea.

En cada gala de eliminación, los participantes reciben una puntuación del 1 al 100, otorgada por el voto del público.

Te piden que hagas una función que reciba una lista de tuplas, donde cada tupla contiene:

• El nombre del participante.

• Su puntuación del 1 al 100.

Se considera como finalistas a los participante cuya puntuación supera los 80 puntos.

La función debe devolver una tupla conformada por:

• El promedio total de las puntuaciones de los finalistas.

• Una lista que contenga los nombres de los finalistas.

Si ningún participante supera los 80 puntos, el promedio deberá ser 0 y la lista de finalistas estará vacía.

Ejemplo: si se recibe la lista [("Helena", 65), ("Joel", 92), ("Malena", 85), ("Pedro", 50)] el programa devuelve (88.5, ['Joel', 'Malena']).
'''

'''    
def finalistas_reality(participantes):
    finalistas = []
    promedio = 0

    for nombre, puntuacion in participantes:
        if puntuacion > 80:
            finalistas.append(nombre)
            promedio += puntuacion

    if len(finalistas) == 0:
        return (0, finalistas)
    
    promedio /= len(finalistas)
    return (promedio, finalistas)

print(finalistas_reality([("Helena", 65), ("Joel", 92), ("Malena", 85), ("Pedro", 50)]))
'''


# ------------------------------ 10 -------------------------------------------------------------------------------------------------

'''
Nuestra gran amiga Valentina está cursando Algebra I para el CBC de Ingeniería Civil y le está costando distinguir cuando dos vectores son perpendiculares.

Nosotros sabemos que para que dos vectores sean perpendiculares se debe cumplir que su producto escalar sea igual a 0. Por ejemplo, si tenemos v = (vₓ, vᵧ) y w = (wₓ, wᵧ), se debe dar que: v * w = vₓ * wₓ + vᵧ * wᵧ = 0.

Para ayudar a Valentina a resolver la guía de ejercicios, le pedimos que nos pase una lista con todos los ejercicios a resolver. Nos pasa una lista de tuplas, donde cada tupla tiene el formato (vₓ, vᵧ, wₓ, wᵧ) y nos pide que le devolvamos solo los vectores que son perpendiculares.

Por ejemplo, si recibimos [(1, 2, 2, -1), (1, 1, 2, 3), (3, 4, 4, -3)] debemos devolver: [(1, 2, 2, -1), (3, 4, 4, -3)].

BONUS: resolver sin ciclos.
'''

'''def es_perpendicular(vector):
    vx, vy, wx, wy = vector
    return vx * wx + vy * wy == 0

def vectores_perpendiculares(lista_vectores):
    return list(filter(es_perpendicular, lista_vectores))
    
print(vectores_perpendiculares([(1, 2, 2, -1), (1, 1, 2, 3), (3, 4, 4, -3)]))'''


# ------------------------------ 11 -------------------------------------------------------------------------------------------------

'''
Ejercicio 11

Una empresa necesita preparar un listado de contacto interno para ciertos empleados. Por motivos de privacidad, no se quiere mostrar el número de teléfono completo de los empleados, sino una versión enmascarada.

Para este listado solo se deben incluir aquellos empleados cuyos números de teléfono correspondan a Argentina (es decir, que empiecen con 54).

Para proteger la información, todos los dígitos del número deben ser reemplazados por asteriscos (*) excepto los últimos tres, que quedarán visibles.

Hay que hacer una función que reciba una lista y realice lo pedido. Por ejemplo, si se recibe la siguiente lista de números:

[541145934696, 34678901234, 5491155554444, 542231234567, 1234567890]

Debe devolver: [*********696", "***********4444", "*********567"]
'''

'''
def proteger_numeros(lista_numeros):
    numeros_protegidos = []
    for numero in lista_numeros:
        numero_str = str(numero)
        if numero_str[:2] == "54":
            protegido = ""
            posicion = 0
            for digito in numero_str:
                if posicion < len(numero_str) - 3:
                    protegido += "*"
                else:
                    protegido += digito

                posicion += 1
                
            numeros_protegidos.append(protegido)
    
    return numeros_protegidos

print(proteger_numeros([541145934696, 34678901234, 5491155554444, 542231234567, 1234567890]))
'''
    

# ------------------------------ 12 -------------------------------------------------------------------------------------------------

'''
Ejercicio 12

Hacer una función que dada la cantidad de ejercicios de un examen y el porcentaje de ejercicios bien resueltos necesarios para
aprobar dicho examen, revise un grupo de exámenes para decidir si están aprobados o no.
El programa debe preguntarle al usuario la cantidad de ejercicios resueltos por un alumno, e imprimir por pantalla el porcentaje
correspondiente aprobado del examen, indicando si aprobó o no. Debe repetir esto mientras el usuario no ingrese el caracter "*".
Nota: El porcentaje se calcula como: ejs resueltos / total ejercicios * 100.
Ejemplo: se recibe 10 ejercicios, y 40 como porcentaje de aprobación:
'''

'''
def aprobacion(ejercicios, porcentaje_aprobacion):
    print(f"> Ejercicios: {ejercicios}. Porcentaje de aprobación: {porcentaje_aprobacion}%")

    usuario = input("> Ingrese los ejercicios resueltos o '*' para salir: ")

    while usuario != "*":
        porcentaje = int(usuario)/ejercicios * 100
        print(f">> Se tiene {porcentaje}% del examen aprobado. Aprobado: {porcentaje >= porcentaje_aprobacion}")

        usuario = input("> Ingrese los ejercicios resueltos o '*' para salir: ")


aprobacion(10, 40)
'''


# ------------------------------ 13 -------------------------------------------------------------------------------------------------

'''
Ejercicio 13

Los docentes de Pensamiento Computacional crean un lenguaje secreto para poder corregir los exámenes a medida que los
entregan, sin que los estudiantes se den cuenta. Cada letra tiene el siguiente significado:
"F": "Desaprobado"
"A": "Aprobado (confirmar nota)"
"C": "Copia (recursa)"
Cualquier otra sigla, se traduce como “Error”.
Al momento de pasar las notas, hay que traducir del lenguaje secreto al significado de cada uno.
Hacer una función que reciba una lista de listas, con los apellidos y la sigla del lenguaje secreto, y devuelva una nueva lista
asignando el significado de cada una. Resolver únicamente con lo visto en la materia hasta el momento y las herramientas que se
dieron para el parcial.
Por ejemplo, si se recibe:
[["Rastrelli", "F"], ["Mendez", "A"], ["Notari", "C"], ["Duzac", "W"]],
se debe devolver
[["Rastrelli", "Desaprobado"], ["Mendez", "Aprobado (confirmar nota)"], ["Notari", "Copia
(recursa)"], ["Duzac", "Error"]].

'''

'''def corregir_examenes(lista_de_alumnos):
    notas = {
        "F": "Desaprobado",
        "A": "Aprobado (confirmar nota)",
        "C": "Copia (recursa)"
    }
    corregido = []

    for alumno, nota in lista_de_alumnos:
        corregido.append([alumno, notas.get(nota, "Error")])

    return corregido

def corregir_examenes2(lista_de_alumnos):
    corregido = []

    for alumno, letra in lista_de_alumnos:
        if letra == "F":
            nota = "Desaprobado"
        elif letra == "A":
            nota = "Aprobado (confirmar nota)"
        elif letra == "C":
            nota = "Copia (recursa)"
        else:
            nota = "Error"

        corregido.append([alumno, nota])

    return corregido


print(corregir_examenes([["Rastrelli", "F"], ["Mendez", "A"], ["Notari", "C"], ["Duzac", "W"]]))
'''


# ------------------------------ 14 -------------------------------------------------------------------------------------------------

'''
Ejercicio 14

Un estudiante de Pensamiento Computacional consigue un trabajo de developer en un banco, y su primera tarea es lograr ocultar
el saldo de la persona.
Hacer una función que reciba una cadena y que cambie todos los dígitos por un "*".
La única limitación es: no se puede usar la función isdigit.
Por ejemplo, si se recibe: "Su saldo en cuenta es: $1500", debe devolver "Su saldo en cuenta es: $****".
'''

'''
def ocultar_saldo(cadena):
    devolucion = ""
    for caracter in cadena:
        if caracter in "0123456789":
            devolucion += "*"
        else:
            devolucion += caracter
    
    return devolucion

print(ocultar_saldo("Su saldo en cuenta es: $1500"))
'''


# ------------------------------ 15 -------------------------------------------------------------------------------------------------

'''
'''

