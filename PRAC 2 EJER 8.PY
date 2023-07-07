#3.	Realizar un sistema utilizando el lenguaje python que solicite dos numeros por teclado y permita elegir entre 3 opciones 
#en un menú que son:
#a.	Mostrar La suma de dos numero
#b.	Mostrar la resta de dos numesios
#c.	Mostrar la multiplicación de 2 numero
print("Calculadora")
num1=input("Ingrese el 1er numero ")
num2=input("Ingrese el 2do numero ")

if num1.isdigit()== True and num2.isdigit() == True:
    print("Ambos son numeros, OK ")
    num1=int(num1)
    num2=int(num2)
    print("Eliga la operacion a realizar")
    print("  1. Para Suma")
    print("  2. Para Resta")
    print("  3. Para Multiplicacion")
    opc=int(input())
    if opc==1:
        res=num1+num2
        print(num1 ,"+" , num2 ,  "=" ,res)
    elif opc==2:
        res=num1-num2
        print(num1, "-", num2, "=" ,res)
    elif opc==3:
        res=num1*num2
        print(num1, "*", num2 ,"=",res)
    else:
        print("Opcion incorrecta")
else:
    print("Uno o ambos valores no son numeros, Error")