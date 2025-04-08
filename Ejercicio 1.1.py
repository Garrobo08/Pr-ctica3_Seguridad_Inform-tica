def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nueva_letra = chr((ord(caracter) - base + desplazamiento) % 26 + base)
            resultado += nueva_letra
        else:
            resultado += caracter
    return resultado

def descifrado_cesar(texto, desplazamiento):
    return cifrado_cesar(texto, -desplazamiento)

def ataque_fuerza_bruta(texto):
    print("\n--- Ataque por fuerza bruta ---")
    for desplazamiento in range(1, 26):
        intento = descifrado_cesar(texto, desplazamiento)
        print(f"Desplazamiento {desplazamiento:2}: {intento}")

def main():
    texto = input("Introduce el texto cifrado (por ejemplo: ROGZZ3P4O_Q1J3): ")
    ataque_fuerza_bruta(texto)

if __name__ == "__main__":
    main()
