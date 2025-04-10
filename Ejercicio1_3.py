# Definición del alfabeto a utilizar
alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = len(alfabeto)

def encode_vigenere(texto, clave):
    """Función para codificar un texto usando el cifrado de Vigenère."""
    resultado = ""
    len_clave = len(clave)
    for i, caracter in enumerate(texto):
        # Buscar el índice del caracter en el alfabeto
        indice_texto = alfabeto.index(caracter)
        # Usar la clave en forma cíclica
        indice_clave = alfabeto.index(clave[i % len_clave])
        # Sumar los índices y obtener el módulo
        indice_codificado = (indice_texto + indice_clave) % n
        resultado += alfabeto[indice_codificado]
    return resultado

def decode_vigenere(texto_cifrado, clave):
    """Función para decodificar un texto cifrado usando el cifrado de Vigenère."""
    resultado = ""
    len_clave = len(clave)
    for i, caracter in enumerate(texto_cifrado):
        indice_cifrado = alfabeto.index(caracter)
        indice_clave = alfabeto.index(clave[i % len_clave])
        # Restar el índice de la clave y ajustar con módulo
        indice_decodificado = (indice_cifrado - indice_clave) % n
        resultado += alfabeto[indice_decodificado]
    return resultado

# Texto cifrado y clave dadas en el enunciado
texto_cifrado = "mvltykycmjfqlu"
clave = "URJC"

# Decodificación
texto_descifrado = decode_vigenere(texto_cifrado, clave)
print("Texto descifrado:", texto_descifrado)

# Ejemplo de codificación (para comprobar que el proceso es reversible)
texto_original = texto_descifrado
texto_re_cifrado = encode_vigenere(texto_original, clave)
print("Texto recifrado:", texto_re_cifrado)
