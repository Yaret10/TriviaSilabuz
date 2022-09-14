import math
#calcula el promedio de 2 numeros
def Ejercicio1():
  num1 = int(input("Ingrese el primer numero:"))
  num2 = int(input("Ingrese el segundo numero:"))
  print("El promedio es:", (num1+num2)/2)

def Ejercicio2():
  num1 = int(input("Ingrese el primer numero:"))
  num2 = int(input("Ingrese el segundo numero:"))
  print(num1**num2)
  
#halle raiz cuadrada
def Ejercicio3():
  num1 = int (input("Ingrese un numero: "))
  print("La raiz caudrada de",num1,"es",math.sqrt(num1))

def Ejercicio4():
  num1 = int(input("Ingrese el primer numero:"))
  num2 = int(input("Ingrese el segundo numero:"))
  print((num1**2 + num2**2)**(1/2))

print("Elija el ejercicio colocando un numero:")
num = int(input())
if num == 1:
  Ejercicio1()
elif num == 2:
  Ejercicio2()
elif num == 3:
  Ejercicio3()
elif num == 4:
  Ejercicio4()

