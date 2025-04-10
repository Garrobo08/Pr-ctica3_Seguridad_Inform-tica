# Definición del alfabeto a utilizar
alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = len(alfabeto)


# Función para codificar un texto usando el cifrado de Vigenère.
def encode_vigenere(texto, clave):
    resultado = ""
    len_clave = len(clave)
    #Recorre cada carácter del texto original
    for i, caracter in enumerate(texto):
        # Buscar el índice del caracter en el alfabeto
        indice_texto = alfabeto.index(caracter)
        indice_clave = alfabeto.index(clave[i % len_clave])
        # Sumar los índices y obtener el módulo
        indice_codificado = (indice_texto + indice_clave) % n
        resultado += alfabeto[indice_codificado]
    return resultado

# Función para decodificar un texto cifrado usando el cifrado de Vigenère.
def decode_vigenere(texto_cifrado, clave):
    resultado = ""
    len_clave = len(clave)
    for i, caracter in enumerate(texto_cifrado):
        indice_cifrado = alfabeto.index(caracter)
        indice_clave = alfabeto.index(clave[i % len_clave])
        # Restar el índice de la clave y ajustar con módulo
        indice_decodificado = (indice_cifrado - indice_clave) % n
        resultado += alfabeto[indice_decodificado]
    return resultado

# Menú principal
if __name__ == "__main__":
    print("CIFRADO Y DESCIFRADO VIGENÈRE")
    print("1. Codificar un texto")
    print("2. Decodificar un texto")
    print("3. Salir")

    opcion = input("Seleccione una opción (1-3): ")

    if opcion == "1":
        texto = input("Introduce el texto a codificar: ")
        clave = input("Introduce la clave, por ejemplo (URJC): ")
        resultado = encode_vigenere(texto, clave)
        print("Texto codificado:", resultado)

    elif opcion == "2":
        print("Introduce el texto cifrado, por ejemplo (mvltykycmjfqlu): ")
        texto_cifrado = input()
        clave = input("Introduce la clave, por ejemplo (URJC): ")
        resultado = decode_vigenere(texto_cifrado, clave)
        print("Texto descifrado:", resultado)

    else:
        print("Saliendo del programa...")