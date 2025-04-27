from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from binascii import unhexlify
from cryptography.hazmat.primitives import padding

# Clave e IV de 16 bytes
key_iv = b"SeguridadInforma"  # 16 bytes para AES-128

def aes_decrypt_cbc(cipher_hex: str) -> str:
    cipher_bytes = unhexlify(cipher_hex)

    cipher = Cipher(algorithms.AES(key_iv), modes.CBC(key_iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(cipher_bytes) + decryptor.finalize()

    # Eliminar el padding PKCS7
    unpadder = padding.PKCS7(128).unpadder()
    decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()

    return decrypted.decode()

# === Prueba con el cifrado dado ===
cifrado_hex = "F55228945ACF1A291DB0C84409852406"
try:
    texto_descifrado = aes_decrypt_cbc(cifrado_hex)
    print("Texto descifrado:", texto_descifrado)
except Exception as e:
    print("Error al descifrar:", e)
