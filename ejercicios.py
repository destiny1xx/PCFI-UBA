# EJERCICIO 2.1
# Guardar el texto “Hola, Mundo!” en una variable e imprimirla por pantalla.
'''saludo = "Hola, Mundo!"
print(saludo)'''


# EJERCICIO 2.2 y 2.3
# Guardar los números 1, 2 y 3 en tres variables distintas e imprimirlos por pantalla.
# Guardar los números 1, 2 y 3 en tres variables distintas y luego sumarlos e imprimir el resultado por pantalla.
#Repetir con las distintas operaciones disponibles que se vieron en la unidad 2: resta, multiplicación, división, división entera, resto, potencia; combinando los números entre sí.
''' n1 = 1
n2 = 2
n3 = 3
print(n1, n2, n3)
print((n1 + n2) // n3)'''


# EJERCICIO 2.4
# Crear un programa que le solicite al usuario: Su nombre y lo imprima por pantalla. Su edad y la imprima por pantalla. Su edad, le sume 1, y la imprima por pantalla.
''' nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print(f"Te llamas {nombre} y tu edad es {edad}, el año que viene vas a cumplir {edad + 1} años!") '''


# EJERCICIO 2.5
# Crear un programa que le solicite al usuario un número, y que imprima el resto obtenido de dividirlo por 2.

''' num = int(input("Ingrese el numero: "))
print(num % 2)'''


# EJERCICIO 2.6
# Escribir un programa que le pida al usuario su año de nacimiento, y que le diga qué edad tiene en el año actual.
''' 
año_nacimiento = int(input("Colocar tu año de nacimiento: "))

edad = 2026 - año_nacimiento

print(f"Naciste el {año_nacimiento} y tu edad actual es {edad}") '''


# EJERCICIO 2.7
# Crear un programa que le solicite al usuario 5 enteros y que muestre por pantalla el promedio de ellos. Hacerlo de dos formas: Primero, usando 5 variables para cada entero. Después, usando una sola variable para almacenar la suma de los 5 enteros. ¿Cómo se te ocurre que podrías hacer?
''' print("Vamos a obtener el promedio de 5 numeros, ingrese cada uno: ")
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))
n4 = int(input("Ingrese el cuarto numero: ")) 
n5 = int(input("Ingrese el quinto numero: "))
print("Gracias!")

sumaenteros = n1 + n2 + n3 + n4 + n5
promedio = sumaenteros // 5
print (f"El promedio entre esos 5 numeros es : {promedio}")'''


# EJERCICIO 2.8
# Crear una función que reciba un número y que devuelva el valor absoluto.
'''def valorabsoluto(num):
    return abs(num)
    
valor = int(input("Ingresa el numero del cual quieres recibir el valor absoluto : "))
print(valorabsoluto(valor))'''


# EJERCICIO 2.9
# Crear una función que reciba un número y que devuelva True si es par, y False si es impar.
''' verificar(num):
    return num % 2 == 0
    
valor = int(input("Ingresa el numero del cual quieres saber si es par o impar : "))
print(verificar(valor))'''


# EJERCICIO 2.10
# Crear una función que reciba un número y un string, y que devuelva ambos concatenados dentro de un nuevo string.
''' def concatenar(num, str):
    return f"{num} {str}" '''


# EJERCICIO 2.11
# Crear una función que reciba dos enteros y que devuelva el resto y el cociente entre ellos.
''' def devolucion(n1, n2):
    return n1 % n2, n1 // n2 '''


# EJERCICIO 2.12
# Crear una función que le pida al usuario su nombre y apellido, e los imprima con el siguiente formato: “Apellido, Nombre”.
''' def formatizar(n, a):
    return f"{a.capitalize()}, {n.capitalize()}"

print("Vamos a formatizar tu Nombre!")
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
print(formatizar(nombre, apellido)) '''


# EJERCICIO 2.13
# Hacer una función que reciba una palabra y devuelva la cantidad de letras que tiene.
'''def contar(palabra):
    return len(palabra)

pedir = input("Ingresar la palabra : ")
print(contar(pedir))'''


# EJERCICIO 2.14
# Hacer una función que reciba una palabra y que imprima los primeros 5 caracteres únicamente. Ejemplo: Si se recibe “pensamiento” se debe imprimir “pensa”.
# Hacer una función que reciba una palabra y que imprima sólo los caracteres ubicados en posiciones pares. Ejemplo: Si se recibe “pensamiento” se debe imprimir “pnaino”.
# Hacer una función que reciba una palabra y que imprima la palabra dada vuelta. Ejemplo: Si se recibe “materia” se debe imprimir “airetam”.
'''def primeros5(palabra):
    return palabra[0:5]

def posicionespar(palabra):
    return palabra[::2]

def darvuelta(palabra):
    return palabra[::-1]

pal = input()
print(posicionespar(pal))
print(primeros5(pal))
print(darvuelta(pal)) '''


# EJERCICIO 2.15
# Hacer una funcion que reciba una palabra, le borre todas las letras “a” e imprima el resultado por pantalla. Pista: usar una función predefinida de Python. Ejemplo: Si se recibe “casa” se debe imprimir “cs”.
''' def borrarA(palabra):
    return palabra.replace("a", "")

valor = input("Ingresa la palabra : ")
print(borrarA(valor))'''


# CLASE 14/4
'''def suma(a,b,c):
    return (a+b+c) // 3

print(suma(1,2,3))'''

'''def gradosakelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

print(gradosakelvin(35))'''

#14/4 ACTIVIDAD EN CASA

# EJERCICIO 2.16
# Analizar qué tipo de dato (o error) se obtiene al hacer las siguientes operaciones:
'''print(5 / 2) 
print(5 // 2)
print(5 % 2)
print(5 ** 2)
print(5.0 / 2)
print(5.0 // 2)
print(5.0 % 2)
print(5.0 ** 2)
print(5 / 2.0)
print(5 // 2.0)
print(5 % 2.0)
print(5 ** 2.0)
print(5.0 / 2.0)
print(5.0 // 2.0)
print(5.0 % 2.0)
print(5.0 ** 2.0)
print("Hola" * 2)
print("Hola" + "2")

#no andan: 
x = "Hola"
x += " mundo"
"Hola" + 2'''


# EJERCICIO 2.17
# Escribir una función que convierta un valor dado en grado Celsius, a Fahrenheit. Recordar que la fórmula para la conversión es: F = 9/5 * C + 32.
# Escribir una función que convierta un valor dado en grados Fahrenheit, a Celsius. Usar la misma fórmula anterior.
''' def convertir_celsius_a_fahrenheit(celsius):
    return (9/5) * celsius + 32

def convertir_fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) / 9/5'''


# EJERCICIO 2.18
# Escribir una función que calcule el área de un triángulo recibiendo como parámetros su base y su altura.
'''def calcular_area_de_triangulo(base, altura):
    area = (base * altura) / 2
    return area '''


# EJERCICIO 2.19
# Escribir una función que calcule la norma de un vector en R3 recibiendo como parámetros las 3 componentes v1, v2, v3 del mismo.
'''def calcular_vector_en_R3(vector1, vector2, vector3):
    R3 = (vector1**2 + vector2**2 + vector3**2) ** 0.5 
    return R3'''


# EJERCICIO 2.20 (OPCIONAL)
# Desafío (no obligatorio): Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas x1, x2, y1 e y2.
'''def calcular_area_de_rectangulo(x1, x2, y1, y2):
    base = abs(x1 - x2)
    altura = abs(y1 - y2)
    
    area_de_rectangulo = base * altura
    return area_de_rectangulo'''


# EVALUACION DE EJERCICIOS 

# CORREGIDOS
'''
def calcular_promedio(n1, n2, n3):
    suma = n1 + n2 + n3
    return suma / 3

def celsius_a_kelvin():
    celsius = input("Ingrese la temperatura en Celsius: ")
    kelvin = celsius + 273.15
    print(kelvin)

def CrearUsuario(nombre, numero):
    usuario = f"{nombre} {numero}"
    return usuario
'''

########################################### UNIDAD 3 ############################################################


# EJERCICIO 3.1
# Escribir una función que, dado un número entero , calcule si es impar o no.
'''def es_impar(num):
    return num % 2 != 0'''
     

# EJERCICIO 3.2
# Escribir una implementación propia de la función , que devuelva el valor absoluto de cualquier valor que reciba. Ejemplo: mi_abs(5) devuelve 5 y mi_abs(-5) devuelve 5. Pista: No se puede usar la función predefinida abs.
'''def mi_abs(num):
    if num < 0:
        return num * (-1)
    return num'''


# EJERCICIO 3.3
# Escribir una función que reciba un número y devuelva True si es entero y False si no lo es. Pista: no se puede usar la función isinstance.
'''def es_entero(num):
    return num == int(num)'''


# EJERCICIO 3.4
# Escribir una función para determinar si una letra recibida es vocal o no. La misma debe devolver un valor booleano. Luego, escribir una función para determinar si una letra es consonante o no.
'''
vocales = ["a", "e", "i", "o", "u"]

def es_vocal(letra):
    if letra.lower() in vocales:
        return True
    
    return False

def es_consonante(letra):
    if letra.lower() not in vocales:
        return True
    
    return False

def es_vocalis(letra):
    if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
        return True
    
    return False

def es_consonanteis(letra):
    if letra.lower() != "a" and letra.lower() != "e" and letra.lower() != "i" and letra.lower() != "o" and letra.lower() != "u":
        return True
    
    return False
'''

# EJERCICIOS 3.5 a y b
# Dado un año, que devuelva si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
# Dado un mes y un año, que devuelva la cantidad de días correspondientes.
'''def es_biciesto(año):
    if (año % 4 == 0 and not año % 100 == 0) or año % 400 == 0:
        return 29
    else:
        return 28
    
Meses_con_30 = [11, 4, 6, 9]
Meses_con_31 = [1, 3, 5, 7, 8, 10, 12]

def devolver_dias(mes, año):
    if mes == 2:
        dias = es_biciesto(año)
        return dias
    
    if mes in Meses_con_30:
        return 30
    elif mes in Meses_con_31:
        return 31
    
    return "Ingresa un mes o año valido."
'''
# EJERCICIO 3.5 c
# Pedirle al usuario su día y mes de cumpleaños. El programa debe imprimir un mensaje indicando a qué signo corresponde el usuario.

'''def devolver_signo_de_usuario():
    dia = int(input("Ingresa tu dia de cumpleaños: "))
    mes = input("Ingresa tu mes de cumpleaños: ")
    mes = mes.lower()

    if (mes == "marzo" and dia >= 21) or (mes == "abril" and dia <= 20):
        print("Tu signo es Aries!")

    elif (mes == "abril" and dia >= 21) or (mes == "mayo" and dia <= 20):
        print("Tu signo es Tauro!")

    elif (mes == "mayo" and dia >= 21) or (mes == "junio" and dia <= 21):
        print("Tu signo es Geminis!")

    elif (mes == "junio" and dia >= 22) or (mes == "julio" and dia <= 23):
        print("Tu signo es Cáncer!")

    elif (mes == "julio" and dia >= 24) or (mes == "agosto" and dia <= 23):
        print("Tu signo es Leo!")

    elif (mes == "agosto" and dia >= 24) or (mes == "septiembre" and dia <= 23):
        print("Tu signo es Virgo!")

    elif (mes == "septiembre" and dia >= 24) or (mes == "octubre" and dia <= 22):
        print("Tu signo es Libra!")

    elif (mes == "octubre" and dia >= 23) or (mes == "noviembre" and dia <= 22):
        print("Tu signo es Escorpio!")

    elif (mes == "noviembre" and dia >= 23) or (mes == "diciembre" and dia <= 21):
        print("Tu signo es Sagitario!")
    
    elif (mes == "diciembre" and dia >= 22) or (mes == "enero" and dia <= 20):
        print("Tu signo es Capricornio!")
    
    elif (mes == "enero" and dia >= 21) or (mes == "febrero" and dia <= 19):
        print("Tu signo es Acuario!")
    
    elif (mes == "febrero" and dia >= 20) or (mes == "marzo" and dia <= 20):
        print("Tu signo es Piscis!")
'''

# EJERCICIO 3.6
# Piedra, papel o tijera: escribir un programa de “Piedra, papel o tijera” tal que sea imposible que el usuario gane. El usuario debe ingresar R (piedra), P (papel), o T (tijera) y la computadora debe siempre ganarle. Las ejecuciones son individuales: el usuario sólo ingresa una sola vez su jugada, el programa le gana, y la ejecución termina.
'''
def piedra_papel_o_tijera():
    print("¡Piedra (R), papel (P) o tijera (T)!")
    jugada = input("Ingrese jugada: ").upper()
    if jugada not in ["R", "P", "T"]:
        print("Esa jugada no está disponible.")
        return
    if jugada == "R":
        print("¡Papel! ¡Gané!")
        return
    if jugada == "P":
        print("¡Tijera! ¡Gané!")
        return
    if jugada == "T":
        print("¡Piedra! ¡Gané!")
        return'''


# EJERCICIO 3.7
# Suponiendo que el primer día del año fue lunes, escribir una función que reciba un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo: si se recibe ‘3’, debe devolver “miércoles”, y si se recibe ‘9’, debe devolver “martes”.
'''
def devolver_dia_de_semana(dia):
    if dia < 1 or dia > 366:
        return "Ingrese un dia valido entre 1 a 366."

    dias = [
        "Lunes",
        "Martes",
        "Miercoles",
        "Jueves",
        "Viernes",
        "Sabado",
        "Domingo",
    ]

    devolucion = (dia - 1) % 7
    return dias[devolucion]
'''

####################### SEGUNDA PARTE DE LA UNIDAD 3  CICLOS #############################

# EJERCICIO 3.1 a y b y c y d y e
# Imprima por pantalla todos los números entre 10 y 20.
'''def imprimir():
    for num in range(10,20):
        print(num)

# Salude a todas las personas de una lista
def saludar_a_personas():
    personas = [
        "Flaminia", 
        "Serena", 
        "Agustina", 
        "Priscila", 
        "Sol", 
        "Agostina", 
        "Iara", 
        "Lu"
    ]

    for persona in personas:
        print(f"Hola {persona}! Vamos a aprender a programar")

# Le pida al usuario que ingrese 5 números y le muestre la suma total de todos ellos.
def sumar_numeros():
    acumulativa = 0
    for i in range (1,6):
        numero = int(input(f"Ingresa el numero n{i} a sumar: "))
        acumulativa += numero

    print(acumulativa) 

# Reciba dos números, y recorra todos los números entre ellos, imprimiendo en pantalla si es par o impar. Por ejemplo, recibiendo 1 y 3, debe imprimir:
def recorrer_numeros(n1, n2):
    for nums in range(n1, n2 + 1):
        if nums % 2 == 0:
            print(f"{nums} es par")
        else:
            print(f"{nums} es impar")
'''

# EJERCICIO 3.2
# Se quiere hacer un programa para enseñar a los niños las tablas de multiplicar del 1 al 10. Crear una función que reciba un número e imprima por pantalla la tabla de multiplicar de ese número. Ejemplo:
'''
def mostrar_tabla_de_multiplicacion(numero):
    numero = int(numero)
    if (numero < 0) or (numero > 10):
        print("Error: El número debe ser positivo y estar entre 1 y 10")
        return
    for mutiplicador in range (1,11):
        print(f"{numero} x {mutiplicador} = {numero * mutiplicador}")'''


# EJERCICIO 3.3
# Crear una función que cante el feliz cumpleaños. Dado un entero, debe imprimir ‘Que los cumplas feliz’ en distintas líneas por esa cantidad de veces.
'''
def cantar_cumpleaños(num):
    num = int(num)
    if num < 0:
        print("El numero tiene que ser mayor a cero")
        return
    
    for cumple in range(num):
        print(f"Que los cumplas feliz\n")'''


# EJERCICIO 3.4
# Programa de cobro
'''
def cobrar():
    total_a_pagar = 500
    print(f"Su total a pagar es : {total_a_pagar}")

    while total_a_pagar > 0:
        print(f"Pendientes: {total_a_pagar}")
        monto_a_pagar = int(input("Ingrese el monto a pagar: "))
        total_a_pagar = total_a_pagar - monto_a_pagar
    
    if total_a_pagar == 0:
        print("Pendientes: 0")
        print("Gracias por su compra.")
    elif total_a_pagar < 0:
        print(f"Su vuelto es {abs(total_a_pagar)}")'''
        
# EJERCICIO 3.5 
# LOOP MULTIPLICAR
'''
def mostrar_tablas_de_multiplicar():
    print("Hola! Esto es Tablas de Multiplicar")
    while True:
        opcion = input("Ingrese un número o 'X' para salir:  ")

        if opcion == "X" or opcion == "x":
            print("Adios!")
            break

        if opcion == str:
            print("Ingrese un numero.")
            continue

        opcion = int(opcion)

        if (opcion < 0) or (opcion > 10):
            print("Error: El número debe ser positivo y estar entre 1 y 10")
            continue

        for mutiplicador in range (1,11):
            print(f"{opcion} x {mutiplicador} = {opcion * mutiplicador}")
'''

# EJERCICIO 3.6
# MANEJO DE CONTRASEÑAS
