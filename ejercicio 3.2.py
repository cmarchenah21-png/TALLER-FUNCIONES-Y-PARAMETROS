def auditar_evento(nivel, *etiquetas, **metadatos):
    print("[" + nivel + "]", end="")

    if etiquetas:
        print(" Tags:", end=" ")
        print(", ".join(etiquetas), end="")

    if metadatos:
        print(" | Metadatos ->", end=" ")

        for dato, valor in metadatos.items():
            print(dato + ":", valor, end=" ")

    print()


auditar_evento(
    "ERROR",
    "#seguridad",
    "#auth",
    usuario="admin",
    ip="192.168.1.50",
    intento=3
)