def calcular_metricas(*numeros, **opciones):
    operacion = opciones.get("operacion", "suma")

    if operacion == "suma":
        resultado = sum(numeros)

    elif operacion == "promedio":
        resultado = sum(numeros) / len(numeros)

    else:
        return "Error: operación no válida"

    if opciones.get("redondear", False):
        decimales = opciones.get("decimales", 0)
        resultado = round(resultado, decimales)

    return resultado


print(calcular_metricas(10, 20, 30, operacion="suma"))


print(calcular_metricas(10, 20, 30, operacion="promedio"))


print(calcular_metricas(
    10, 20, 25,
    operacion="promedio",
    redondear=True,
    decimales=2
))