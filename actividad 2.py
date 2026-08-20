ventas_dia = ["Electronica", "Ropa", "Electronica", "Hogar", "Ropa", "Electronica", "Juguetes", "Hogar"]

categorias_unicas = set(ventas_dia)

print("Categorias unicas:")
print("Categorias_unicas")

conteo = {}

for categoria in ventas_dia:
    if categoria in conteo: 
        conteo[categoria] += 1
    else:
        conteo[categoria] = 1

print("\nCantidad de ventas por categoria:")
for categoria, cantidad in conteo.items():
    print(categoria, ":", cantidad)

categoria_mas_vendida = max(conteo, key=conteo.get)

print("\nCategoria mas vendida:", categoria_mas_vendida)
print("Cantidad de ventas:", conteo[categoria_mas_vendida])