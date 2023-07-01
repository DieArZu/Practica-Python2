#3.	Crear un programa utilizando Python que permita determinar el salario a pagar a un empleado teniendo 
# como entradas el salario diario y el número de días trabajados. Tenga en cuenta que al empleado se le 
# #debe descontar el 10% por concepto de pensión y 15% por concepto de salud.
print("Calculo de salario")
salario=float(input("Ingrese el salario diario del colaborador: "))
dias=float(input("Ingrese la cantidad de dias laborados: "))
tot=salario*dias
pension=tot*0.1
salud=tot*0.15
neto=tot-pension-salud
print("El salario bruto es de: ", tot)
print("Rebajo por Pension:     -",pension)
print("Rebajo por salud:       -", salud)
print("Salario neto a pagar:   ",neto)
