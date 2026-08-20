def generar_reporte(titulo, *secciones):
    print("Título:", titulo)

    for seccion in secciones:
        print("Sección:", seccion)


generar_reporte(
    "Reporte de ventas",
    *["Introducción", "Ventas", "Conclusiones"]
)