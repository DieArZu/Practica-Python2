#1.	Crear un programa utilizando Python que solicite 2 números por el teclado y 
#debe de mostrar en pantalla la suma, resta, multiplicación y división de ellos.

print("Calculadora de 2 numeros")
num1=input("Ingrese el 1er numero ")
num2=input("Ingrese el 2do numero ")

if num1.isdigit()== True and num2.isdigit() == True:
    print("Ambos son numeros, OK ")
    num1=int(num1)
    num2=int(num2)
    sum=num1+num2
    print(num1 ,"+" , num2 ,  "=" ,sum)
    res=num1-num2
    print(num1, "-", num2, "=" ,res)
    mult=num1*num2
    print(num1, "*", num2 ,"=",mult)
else:
    print("Uno o ambos valores no son numeros, Error")