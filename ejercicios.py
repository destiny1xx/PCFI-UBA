# EJERCICIO 2.1
'''saludo = "Hola, Mundo!"
print(saludo)'''


# EJERCICIO 2.2 y 2.3
''' n1 = 1
n2 = 2
n3 = 3
print(n1, n2, n3)
print((n1 + n2) // n3)'''

# EJERCICIO 2.4
''' nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print(f"Te llamas {nombre} y tu edad es {edad}, el año que viene vas a cumplir {edad + 1} años!") '''

# EJERCICIO 2.5
''' num = int(input("Ingrese el numero: "))
print(num % 2)'''

# EJERCICIO 2.6
''' 
año_nacimiento = int(input("Colocar tu año de nacimiento: "))

edad = 2026 - año_nacimiento

print(f"Naciste el {año_nacimiento} y tu edad actual es {edad}") '''

# EJERCICIO 2.7
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
''' def valorabsoluto(num):
    if num >= 0:
        return num
    else:
        return -num
    
valor = int(input("Ingresa el numero del cual quieres recibir el valor absoluto : "))
print(valorabsoluto(valor))'''

# EJERCICIO 2.9
''' def verificar(num):
    return num % 2 == 0
    
valor = int(input("Ingresa el numero del cual quieres saber si es par o impar : "))
print(verificar(valor))'''

# EJERCICIO 2.10
''' def concatenar(num, str):
    return f"{num} {str}" '''

# EJERCICIO 2.11
''' def devolucion(n1, n2):
    return n1 % n2, n1 // n2 '''

# EJERCICIO 2.12
''' def formatizar(n, a):
    return f"{a.capitalize()}, {n.capitalize()}"

print("Vamos a formatizar tu Nombre!")
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
print(formatizar(nombre, apellido)) '''

# EJERCICIO 2.13
'''def contar(palabra):
    return len(palabra)

pedir = input("Ingresar la palabra : ")
print(contar(pedir))'''

# EJERCICIO 2.14
''' def primeros5(palabra):
    return palabra[0:5]

def posicionespar(palabra):
    return palabra[::2]

def darvuelta(palabra):
    return palabra[::-1]

pal = input()
print(posicionespar(pal))
print(primeros5(pal))
print(darvuelta(pal))'''

# EJERCICIO 2.15
''' def borrarA(palabra):
    return palabra.replace("a", "")

valor = input("Ingresa la palabra : ")
print(borrarA(valor))'''



