import re

def contraseña_segura(password):
    if len(password) < 8:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    return True


def registrar_usuario():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cedula = input("Identificación: ")
    edad = input("Edad: ")
    usuario = input("Usuario (correo): ")
    password = input("Contraseña: ")

    if not contraseña_segura(password):
        print("Contraseña insegura")
        return

    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{nombre},{apellido},{cedula},{edad},{usuario},{password}\n")

    print("Usuario registrado correctamente")


def iniciar_sesion():
    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    with open("usuarios.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if datos[4] == usuario and datos[5] == password:
                print("Inicio de sesión exitoso")
                return

    print("Credenciales incorrectas")
