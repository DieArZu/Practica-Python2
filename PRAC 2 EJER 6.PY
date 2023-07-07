#1.	Utilizando operadores lógicos determine si una cadena de texto introducida por el usuario tiene una logitud mayor o igual a 3 
#o menor igual a 12, se debe de mostrar True o false.
frase=str(input("Ingrese la palbra o frase a medir:  " ))
tama=len(frase)
print(tama)
print(tama>=3 and tama<=12)
#if tama>=3 and tama<=12:
#    print("True")
#else:
#    print("false")