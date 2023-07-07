#5.	Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo.
#El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
#Si se cumple Pitágoras entonces es triángulo rectángulo
#Si sólo dos lados del triángulo son iguales entonces es isósceles.
#Si los 3 lados son iguales entonces es equilátero.
#Si no se cumple ninguna de las condiciones anteriores, es escaleno.
print("Programa validacion de Triangulo")
a=int(input("Ingrese la medida del 1er lado: "))
b=int(input("Ingrese la medida del 2do lado: "))
c=int(input("Ingrese la medida del 3er lado: "))
#validamos si las medidas realmente pueden formar un triangulo 
if a+b>c and a+c>b and b+c>a:
   # Es rectangulo?
   hipo=max(a,b,c)
   if hipo==a:
      d=(b**2+c**2)**(1/2)
      if a==d:
         print("Es rectangulo")
      elif a==c and a==b:
         print("Es equilatero")
      elif a==b and a!=c:
         print("Es isoceles")
      elif a==c and a!=b:
         print("Es isoceles")
      elif b==c and a!=b:
         print("Es isoceles")
      else:
         print("Es escaleno")
   
   #rev en b
   elif hipo==b:
      d=(b**2+a**2)**(1/2)
      if b==d:
         print("Es rectangulo")
      elif b==a and b==c:
         print("Es equilatero")
      elif b==a and b!=c:
         print("Es isoceles")
      elif b==c and a!=b:
         print("Es isoceles")
      elif a==c and b!=a:
         print("Es isoceles")
      else:
         print("Es escaleno") 

#rev en c
   elif hipo==c:
      d=(b**2+a**2)**(1/2)
      if c==d:
         print("Es rectangulo")
      elif c==a and c==b:
         print("Es equilatero")
      elif c==a and c!=b:
         print("Es isoceles")
      elif c==b and c!=a:
         print("Es isoceles")
      elif a==b and c!=a:
         print("Es isoceles")
      else:
         print("Es escaleno") 

 #No puede ser un triangulo   
else:
   print("Las medidas dadas no pueden formar un triangulo")
   
