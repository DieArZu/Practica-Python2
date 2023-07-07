#7.	Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales.
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
print("Programa de calculo de impuesto")
edad=int(input("Ingrese la edad del cliente "))
ingresos=int(input("Ingrese el igreso del cliente "))
if edad>=16 and ingresos>=1000:
    print("El cliente debe tributar")
else:
    print("El cliente esta exonerado del impuesto")