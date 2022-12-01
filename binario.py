#Realiza, utilizando Python 3, un programa llamado binario.py 
#que pida al usuario que introduzca un número binario e imprima por pantalla el número en formato decimal.
#Para desarrollar el programa, es necesario que desarrolles una función con la siguiente cabecera:
#def esBinario(strbinario)
#Devuelve True o False si la cadena de caracteres (strbinario) que se ha pasado como parámetro contiene una cadena binaria.
#Ejemplo de esBinario:
#print(esBinario("1001")) True
#print(esBinario("Hola")) False

def comprobacion(string):
     
    p = set(string)
 
    s = {'0', '1'}

    if s == p or p == {'0'} or p == {'1'}:
        return True
    else:
        return False


def esBinario(binario):

    posicion = 0
    decimal = 0

    binario = binario[::-1]

    for digito in binario:
        multiplicador = 2*posicion
        decimal += int(digito) * multiplicador
        posicion += 1

    return decimal

numeroUsuario = str(input("Introduce un numero: "))

if comprobacion(numeroUsuario):
    print(esBinario(numeroUsuario))
else:
    print("El número no es binario")

