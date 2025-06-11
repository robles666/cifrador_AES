import tkinter as tk
from tkinter import messagebox, scrolledtext
from cryptography.fernet import Fernet

# Funciones
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as f:
        f.write(clave)
    messagebox.showinfo("Clave generada", "🔐 Clave guardada como 'clave.key'")

def cargar_clave():
    try:
        with open("clave.key", "rb") as f:
            return Fernet(f.read())
    except FileNotFoundError:
        messagebox.showerror("Error", "Primero debes generar una clave")
        return None

def cifrar():
    fernet = cargar_clave()
    if not fernet:
        return
    texto = texto_entrada.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Advertencia", "El texto está vacío")
        return
    cifrado = fernet.encrypt(texto.encode())
    texto_resultado.delete("1.0", tk.END)
    texto_resultado.insert(tk.END, cifrado.decode())

def descifrar():
    fernet = cargar_clave()
    if not fernet:
        return
    texto = texto_entrada.get("1.0", tk.END).strip()
    try:
        descifrado = fernet.decrypt(texto.encode()).decode()
        texto_resultado.delete("1.0", tk.END)
        texto_resultado.insert(tk.END, descifrado)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo descifrar:\n{e}")

# Interfaz
ventana = tk.Tk()
ventana.title("Cifrado Fernet (AES)")

tk.Button(ventana, text="🔐 Generar clave", command=generar_clave).pack(pady=5)

tk.Label(ventana, text="Texto de entrada (claro o cifrado):").pack()
texto_entrada = scrolledtext.ScrolledText(ventana, width=60, height=5)
texto_entrada.pack(pady=5)

tk.Button(ventana, text="🔒 Cifrar", command=cifrar).pack(pady=5)
tk.Button(ventana, text="🔓 Descifrar", command=descifrar).pack(pady=5)

tk.Label(ventana, text="Resultado:").pack()
texto_resultado = scrolledtext.ScrolledText(ventana, width=60, height=5)
texto_resultado.pack(pady=5)

ventana.mainloop()
