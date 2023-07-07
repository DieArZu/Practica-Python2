#9.	Realizar un sistema utilizando el lenguaje Python que solicite dos palabras y diga si riman o no. 
#Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene 
#que decir que riman un poco y si no, que no riman.
print("Rima de Palabras")
palabra1=input("Ingrese la 1er palabra: ")
palabra2=input("Ingrese la 2da palabra: ")
if palabra1[-3:] == palabra2[-3:]:
    print("Las palabras si riman")

elif palabra1[-2:] == palabra2[-2:]:
    print("Las palabras si riman un poco")

else:
    print("Las palabras NO riman")
