def xor_cipher(texto, clave):
    """Función que aplica XOR entre cada caracter de 'texto' y la clave, repitiéndola cíclicamente."""
    resultado = ""
    len_clave = len(clave)
    for i, caracter in enumerate(texto):
        # Se obtiene el código ASCII del caracter y del caracter correspondiente de la clave.
        ascii_texto = ord(caracter)
        ascii_clave = ord(clave[i % len_clave])
        # Se aplica el operador XOR y se convierte de vuelta a caracter.
        resultado += chr(ascii_texto ^ ascii_clave)
    return resultado

# Cadena cifrada proporcionada y la clave para verificar el funcionamiento
texto_cifrado = "({!+8b*+"
clave = "XOR"

# Decodificación: al aplicar XOR con la misma clave se recupera el texto original
texto_descifrado = xor_cipher(texto_cifrado, clave)
print("Texto descifrado:", texto_descifrado)

# Para comprobar la reversibilidad, se vuelve a codificar el texto descifrado
texto_re_cifrado = xor_cipher(texto_descifrado, clave)
print("Texto recifrado:", texto_re_cifrado)
