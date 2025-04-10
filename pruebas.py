import base64


def codificar_base64(texto):
    # Convertir el texto a bytes (UTF-8)
    bytes_texto = texto.encode('utf-8')
    # Codificar en Base64
    bytes_codificados = base64.b64encode(bytes_texto)
    # Devolver como string
    return bytes_codificados.decode('utf-8')


def decodificar_base64(texto_codificado):
    # Convertir el texto codificado a bytes
    bytes_codificados = texto_codificado.encode('utf-8')
    # Decodificar de Base64
    bytes_decodificados = base64.b64decode(bytes_codificados)
    # Devolver como string
    return bytes_decodificados.decode('utf-8')



def main():
    print("Codificador y Decodificador Base64")
    print("1. Codificar texto a Base64")
    print("2. Decodificar texto desde Base64")

    opcion = input("Seleccione una opción (1/2): ")

    if opcion == '1':
        texto = input("Introduzca el texto a codificar: ")
        resultado = codificar_base64(texto)
        print("\nTexto codificado:")
        print(resultado)
    elif opcion == '2':
        texto = input("Introduzca el texto a decodificar: ")
        resultado = decodificar_base64(texto)
        print("\nTexto decodificado:")
        print(resultado)
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()