def crear_perfil_usuario(nombre, email, rol):
    if "@" not in email:
        return "Error: el email no contiene el símbolo @"

    usuario = {
        "nombre": nombre,
        "email": email,
        "rol": rol
    }

    return usuario


resultado1 = crear_perfil_usuario("Laura Gómez", "laura@empresa.com", "Desarrolladora")
print(resultado1)

resultado2 = crear_perfil_usuario(
    nombre="Carlos",
    email="carlos_sin_arroba",
    rol="Admin"
)
print(resultado2)