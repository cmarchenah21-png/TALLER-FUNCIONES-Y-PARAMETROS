def ejecutar_mision(nombre_tarea, al_exito=None, al_error=None):
    try:
        print("Ejecutando tarea:", nombre_tarea)

    
        resultado = 10 / 2

        if al_exito:
            al_exito(nombre_tarea, resultado)

    except Exception as error:
        if al_error:
            al_error(nombre_tarea, str(error))


def exito(nombre_tarea, resultado):
    print("La tarea", nombre_tarea, "fue exitosa.")
    print("Resultado:", resultado)


def error(nombre_tarea, mensaje_error):
    print("La tarea", nombre_tarea, "falló.")
    print("Error:", mensaje_error)


ejecutar_mision("Calcular operación", exito, error)