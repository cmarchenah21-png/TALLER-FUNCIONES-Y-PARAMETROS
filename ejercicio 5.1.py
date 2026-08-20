def procesar_coleccion(lista_datos, funcion_transformacion, funcion_filtro):
    resultado = []

    for numero in lista_datos:
        if funcion_filtro(numero):
            resultado.append(funcion_transformacion(numero))

    return resultado


def es_par(numero):
    return numero % 2 == 0


def duplicar(numero):
    return numero * 2

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

resultado = procesar_coleccion(numeros, duplicar, es_par)

print(resultado)