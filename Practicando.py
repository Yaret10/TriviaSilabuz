#--*, -, +, / ejercios 1
num1 = int (input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
operador = input("Ingrese operador matemático: ")
resultado = 0

while operador not in ("*","+","-","/"):
  resultado = "operador invalido"
  operador = input("Resultado invalido. Porfavor ingrese +, -, *, /: ")
  

if operador == "*":
  resultado = num1 * num2
  print("Resultado:",resultado)
elif operador == "+":
  resultado = num1 + num2
  print("Resultado:",resultado)
elif operador == "-":
  resultado = num1 - num2
  print("Resultado:",resultado)
elif operador == "/":
  resultado = num1 / num2
  print("Resultado:",resultado)
