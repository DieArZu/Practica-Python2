#5.	Crear una aplicación usando python que resuelva el siguiente problema, la jornada de trabajo es de 48 horas, 
#se debe de solicitar las horas trabajadas y el pago por hora, si las horas sobrepasan la jornada semanal, 
#deben de pagar las horas extras el doble.
print("Jornada de trabajo")
horastrabajadas=float(input("Ingrese la cantidad de horas trabajadas en la semana: "))
costohora=float(input("Ingrese el valor de la hora laborada: "))
if horastrabajadas<=48:
    salario=horastrabajadas*costohora
    print("El salario de esta semana es de: ",salario)

elif horastrabajadas>48:
    extras=(horastrabajadas-48)*costohora*2
    salario=48*costohora
    salarioneto=extras+salario
    print("El salario de esta semana es de: ",salarioneto)