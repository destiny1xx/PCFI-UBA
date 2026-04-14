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
''' vocales = ["a", "e", "i", "o", "u"]

def es_vocal(letra):
    if letra.lower() in vocales:
        return True
    
    return False

def es_consonante(letra):
    if letra.lower() not in vocales:
        return True
    
    return False '''



