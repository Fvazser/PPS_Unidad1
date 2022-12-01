#Crea un programa que reciba un número del 1 al 20 introducido por el usuario y compruebe si está
#dentro de la siguiente lista: [6,14,11,3,2,1,15,19]. Implementa una función que se asegure que el
#número introducido por el usuario está en el rango indicado y otra que compruebe si está dentro
#de la lista. Trata de crear las funciones de forma que puedan ser reutilizadas lo máximo posible en
#otros programas.

lista = [6, 14, 11, 3, 2, 1, 15, 19]

numero_introducido = int (input ("Introduce un numero del 1 al 20: "))

def estaEnLista (numero, lista):
    if numero in lista:
        print(f"El numero {numero} está en la lista")
    else:
        print("El numero no está en lista")

estaEnLista (numero_introducido, lista)

def estaEnRango (valor, minimo, maximo):
    if valor > minimo or valor < maximo:
        print(f"El numero {valor} está en rango")
    else:
        print("No esta en rango")

estaEnRango (numero_introducido, 5, 20)

