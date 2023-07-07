#2.	Realizar un sistema utilizando el lenguaje python que solicite 2 numeros por teclado y determine los siguientes aspectos:
#a.	Si los dos numeros son iguales
#b.	Si los dos numeros son diferentes
#c.	Si el primero es mayor que el segundo
#d.	Si el segundo es mayor o igual que el primero
#e.	Si son numeros o letras
print("Comparacion de numeros")
num1=input("Ingrese el 1er numero ")
num2=input("Ingrese el 2do numero ")
#isdigit() : Devuelve True si i solamente contiene caracteres numéricos.
#isalpha() : Devuelve True si i solamente contiene caracteres del alfabeto.
if num1.isdigit()== True and num2.isdigit() == True:
    print("Ambos son numeros, OK ")
    if num1==num2:
        print("a.Los numeros son iguales")
    else:
        print("b.Los numeros son diferentes")
    if num1>num2:
        print("c.El 1ero es mayor q el 2do")
    else:
        print("d.El 2do es mayor que el 1ero")
else:
    print("Uno o ambos valores no son numeros, Error")


