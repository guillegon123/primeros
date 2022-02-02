# Forma de hacer aplicando buenas practicas
def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escriba una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palíndromo")
    else:
        print("No es palíndromo")


if __name__ == "__main__":
    run()


# MI PROPUESTA
#def alistar (texto):
#    nuevo = texto
#    nuevo = nuevo.lower()
#    nuevo=nuevo.strip() # strip me quita los espacio al final de las palabras
#    nuevo=nuevo.replace(" ","")
#    return nuevo

#palabra = input("Escribe una palabra: ")
#if alistar(palabra)== alistar(palabra)[::-1]:
#    print("Es palíndromo")
#else:
#    print("no es palindromo")
