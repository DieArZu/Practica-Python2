#4.	Crear un programa utilizando Python que permita calcular el valor final a pagar en una 
#súper tienda en donde se aplican los siguientes descuentos:
#a) Por compras entre 10000 y 20000 el 10%
#b) Por compras entre 20001y 50000 el 30%
#c) Por compras superiores a 50000 el 50%("
print("Calculo de descuento segun compras")
compra=float(input("Ingrese el monto de la compra: $"))
if compra<10000:
    print("Compra sin descuento: $",compra)

elif compra>=10000 and compra<=20000:
    desc=compra*0.1
    neto=compra-desc
    print("Compra con 10% de descuento")
    print("Monto del descuento $",desc)
    print("El precio final de la compra es: $",neto)

elif compra>=20001 and compra<50000:
    desc=compra*0.3
    neto=compra-desc
    print("Compra con 30% de descuento")
    print("Monto del descuento $",desc)
    print("El precio final de la compra es: $",neto)

elif compra>=50000:
    desc=compra*0.5
    neto=compra-desc
    print("Compra con 50% de descuento")
    print("Monto del descuento $",desc)
    print("El precio final de la compra es: $",neto)