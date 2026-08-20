def buscar_clave_profunda(estructura, clave_objetivo):
    if clave_objetivo in estructura:
        return estructura[clave_objetivo]

    for clave in estructura:
        valor = estructura[clave]

        if isinstance(valor, dict):
            resultado = buscar_clave_profunda(valor, clave_objetivo)

            if resultado is not None:
                return resultado

    return None


datos = {
    "nombre": "Carlos",
    "usuario": {
        "edad": 20,
        "direccion": {
            "ciudad": "Bogota",
            "codigo": 110111
        }
    }
}


resultado = buscar_clave_profunda(datos, "ciudad")

print(resultado)