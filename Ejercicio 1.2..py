import base64
#Función para el codificador en base64
def codificar_base64(texto):
    # Convertir el texto a bytes (UTF-8)
    bytes_texto = texto.encode('utf-8')
    # Codificar en Base64
    bytes_codificados = base64.b64encode(bytes_texto)
    # Devolver como string
    return bytes_codificados.decode('utf-8')

#Función para la decodificación en base64
def decodificar_base64(texto_codificado):
    try:
        # Convertir el texto codificado a bytes
        bytes_codificados = texto_codificado.encode('utf-8')
        # Decodificar de Base64
        bytes_decodificados = base64.b64decode(bytes_codificados)
        # Devolver como string
        return bytes_decodificados.decode('utf-8')
    except Exception as e:
        return f"Error al decodificar: {str(e)}"

#Programa principal
if __name__ == "__main__":
    print("Codificador y Decodificador Base64")
    print("1. Codificar texto a Base64")
    print("2. Decodificar texto desde Base64")
    print("3. Salir")

    opcion = input("Seleccione una de las opciones: ")
    if opcion == "1":
        texto = input("Introduzca el texto a codificar, por ejemplo (VVJKQ3tTTTRMTF9CNFMzXzY0fQ==): ")
        resultado = codificar_base64(texto)
        print("\n Texto codificado: ")
        print(resultado)
    elif opcion == "2":
        texto = input("Introduzca el texto a decodificar, por ejemplo (VVJKQ3tTTTRMTF9CNFMzXzY0fQ==): ")
        resultado = decodificar_base64(texto)
        print("\n Texto decodificado: ")
        print(resultado)
    else:
        print("Saliendo...")