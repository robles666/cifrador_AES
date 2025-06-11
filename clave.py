from cryptography.fernet import Fernet

# -----------------------
# Función para generar clave
# -----------------------
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)
    print("🔐 Clave generada y guardada como 'clave.key'.")

# -----------------------
# Función para cargar clave
# -----------------------
def cargar_clave():
    with open("clave.key", "rb") as archivo_clave:
        clave = archivo_clave.read()
    return Fernet(clave)

# -----------------------
# Función para cifrar mensaje
# -----------------------
def cifrar_mensaje(mensaje):
    fernet = cargar_clave()
    mensaje_cifrado = fernet.encrypt(mensaje.encode())
    return mensaje_cifrado

# -----------------------
# Función para descifrar mensaje
# -----------------------
def descifrar_mensaje(mensaje_cifrado):
    fernet = cargar_clave()
    mensaje_descifrado = fernet.decrypt(mensaje_cifrado).decode()
    return mensaje_descifrado

# -----------------------
# Prueba del sistema
# -----------------------
if __name__ == "__main__":
    print("1. Generando clave...")
    generar_clave()

    texto = "Este es un mensaje secreto"
    print(f"\n2. Texto original: {texto}")

    cifrado = cifrar_mensaje(texto)
    print(f"\n3. Texto cifrado: {cifrado}")

    descifrado = descifrar_mensaje(cifrado)
    print(f"\n4. Texto descifrado: {descifrado}")
