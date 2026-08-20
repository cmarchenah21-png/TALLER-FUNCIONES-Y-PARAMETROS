nombre = input("Ingrese el nombre del cliente: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad adquirida: "))
vip = input("¿Tiene membersia VIP? (si/no): ").lower() == "si"

total = precio * cantidad

if cantidad >= 5 and vip:
    descuento = 0.25
elif cantidad >= 5 or vip:
    descuento = 0.15
else:
    descuento = 0.00

valor_descuento = total * descuento
total_pagar = total - valor_descuento

print("\n===== RESUMEN DEL COBRO =====")
print("Cliente:", nombre)
print("Presio unitario: $", precio)
print("Cantidad:", cantidad)
print("Membersia VIP:", vip)
print("Total antes del descuento: $", total)
print("Descuento aplicado:", descuento * 100, "%")
print("Valor del descuento: $", valor_descuento)
print("Total a pagar: $", total_pagar)