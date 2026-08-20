def aplicar_impuesto(tasa_iva, lista_precios):
    print("Antes de la función:")
    print("Tasa IVA:", tasa_iva)
    print("Lista de precios:", lista_precios)

    
    for i in range(len(lista_precios)):
        lista_precios[i] = lista_precios[i] * (1 + tasa_iva)

    
    tasa_iva = 0.50

    print("\nDespués de la función:")
    print("Tasa IVA:", tasa_iva)
    print("Lista de precios:", lista_precios)


tasa = 0.19
precios = [10000, 20000, 30000]

aplicar_impuesto(tasa, precios)

print("\nFuera de la función:")
print("Tasa IVA:", tasa)
print("Lista de precios:", precios)