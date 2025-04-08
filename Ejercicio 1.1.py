#Función para cifrar un texto usando el Cifrado César con un desplazamiento específico
def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    #Recorremos cada carácter del texto
    for caracter in texto:
        if caracter.isalpha(): # Si el carácter es una letra
            base = ord('A') if caracter.isupper() else ord('a')
            nueva_letra = chr((ord(caracter) - base + desplazamiento) % 26 + base) #Calcula la nueva letra después de aplicar el desplazamiento
            resultado += nueva_letra
        else: #Si no es una letra, no se cambia
            resultado += caracter
    return resultado

#Función para descifrar un texto con el Cifrado César
def descifrado_cesar(texto, desplazamiento):
    return cifrado_cesar(texto, -desplazamiento) #desplazamiento negativo, así invierte el cifrado

#Función ataque de fuerza bruta para encontrar el desplazamiento
def ataque_fuerza_bruta(texto):
    print("\n--- Ataque por fuerza bruta ---")
    for desplazamiento in range(1, 26): #Probamos todos los desplazamientos posibles.
        resultado = descifrado_cesar(texto, desplazamiento)
        print(f"Desplazamiento {desplazamiento:2}: {resultado}")

#Función principal
if __name__ == "__main__":
    texto = input("Introduce el texto cifrado (por ejemplo: ROGZZ3P4O_Q1J3): ")
    ataque_fuerza_bruta(texto)
