from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from binascii import hexlify, unhexlify

# Clave e IV de 16 bytes (128 bits)
key_iv = b"SeguridadInforma"


# Función para cifrar en AES-128 CBC
def aes_encrypt_cbc(plaintext: str) -> str:
    # Aplicar padding PKCS7
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    # Crear el objeto Cipher
    cipher = Cipher(algorithms.AES(key_iv), modes.CBC(key_iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(padded_data) + encryptor.finalize()

    # Convertir a hexadecimal
    return hexlify(encrypted).decode()


# Función para descifrar en AES-128 CBC
def aes_decrypt_cbc(cipher_hex: str) -> str:
    cipher_bytes = unhexlify(cipher_hex)

    cipher = Cipher(algorithms.AES(key_iv), modes.CBC(key_iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(cipher_bytes) + decryptor.finalize()

    # Eliminar el padding PKCS7
    unpadder = padding.PKCS7(128).unpadder()
    decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()

    return decrypted.decode()


# Función principal que interactúa con el usuario
def main():
    while True:
        # Menú para elegir cifrado o descifrado
        print("\nSeleccione una opción:")
        print("1. Cifrar texto")
        print("2. Descifrar texto")
        print("3. Salir")

        opcion = input("Ingrese su opción (1/2/3): ")

        if opcion == "1":
            # Cifrado
            texto = input("Ingrese el texto a cifrar: ")
            cifrado = aes_encrypt_cbc(texto)
            print("Texto cifrado (hex):", cifrado)

        elif opcion == "2":
            # Descifrado
            texto_hex = input(
                "Ingrese el texto cifrado en formato \nhexadecimal por ejemplo: F55228945ACF1A291DB0C84409852406: ")
            descifrado = aes_decrypt_cbc(texto_hex)
            print("Texto descifrado:", descifrado)

        elif opcion == "3":
            # Salir del programa
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, intente nuevamente.")


# Ejecutar el programa
if __name__ == "__main__":
    main()
