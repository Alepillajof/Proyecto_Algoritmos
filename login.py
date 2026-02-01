def contraseña_segura(c):
    mayuscula = False
    minuscula = False
    numero = False

    for x in c:
        if x >= 'A' and x <= 'Z':
            mayuscula = True
        if x >= 'a' and x <= 'z':
            minuscula = True
        if x >= '0' and x <= '9':
            numero = True

    if mayuscula and minuscula and numero:
        return True
    else:
        return False


def registrar_usuario():
    print("REGISTRO")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    identificacion = input("Ingrese su cedula: ")
    edad = input("Ingrese su edad: ")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese una contrasenia: ")

    if contraseña_segura(contraseña) == False:
        print("Contraseña no válida")
        return

    archivo = open("usuarios.txt", "a")
    archivo.write("Cliente|" + usuario + "|" + contraseña + "\n")
    archivo.close()

    print("Registro exitoso")


def iniciar_sesion():
    print("INICIO DE SESIÓN")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    archivo = open("usuarios.txt", "r")
    for linea in archivo:
        datos = linea.strip().split("|")
        if datos[1] == usuario and datos[2] == contraseña:
            archivo.close()
            return datos[0]

    archivo.close()
    return None


while True:
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        rol = iniciar_sesion()
        if rol != None:
            print("Bienvenido", rol)
        else:
            print("Credenciales incorrectas")
    elif opcion == "3":
        print("Saliendo...")
        break
