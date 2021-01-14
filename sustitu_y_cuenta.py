def sustitu_y_cuenta(txt,carin,caroun):
    """ La funcion recibe una cadena de caracteres junto a 2 caracteres 'carin' y 'carout' y devuelve un resultado
    compuesto por la cadena de caracteres modificada y la cantidad de caracteres que se reemplazaron """

    cadena_nueva = ""
    contador = 0
    for letra in txt:
        if letra == carin:
         cadena_nueva = cadena_nueva + caroun
         contador += 1
        else:
            cadena_nueva = cadena_nueva + letra
    return cadena_nueva, contador
    
def main():

    caracter_sustituido = input("Introduzca un caracter a sustituir: ")

    caracter_nuevo = input("\nIntroduzca por cual sera sustituido: ")

    palabra = ''
    cantidad_sustituciones = 0

    palabra = input("\nIntroduzca una palabra a sustituir: ")

    while palabra != '*':

        palabra_nueva, car_sustituidos = sustitu_y_cuenta(palabra, caracter_sustituido, caracter_nuevo)

        print("\nUsted introdujo la palabra '{}', su palabra sustituida quedo '{}'\nSe sustituyeron {} caracteres".format(palabra, palabra_nueva,car_sustituidos))
        print("\nPara finalizar introduzca '*'")

        cantidad_sustituciones += car_sustituidos

        palabra = input("\nIntroduzca una palabra a sustituir: ")
    
    print("\nSe realizaron un total de {} sustituciones".format(cantidad_sustituciones))

    pausa = input("Presione enter para salir...")

main()
