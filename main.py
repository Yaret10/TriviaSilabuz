import random
#Reglamento de la trivia:
  #1ra pregunta 
    #RC = 10 puntos + (0,3) puntos aleatorios
    #RI = -(5 puntos + (0,3) puntos aleatorios)
  #2da pregunta
    #RC = 10 puntos + (0,5) puntos aleatorios
    #RI = -(5 puntos + (0,5) puntos aleatorios)
  #3da pregunta
    #RC = 10 puntos + (0,7) puntos aleatorios
    #RI = -(5 puntos + (0,7) puntos aleatorios)
  #4da pregunta
    #RC = 10 puntos + (0,10) puntos aleatorios
    #RI = -(5 puntos + (0,10) puntos aleatorios)
# +5 puntos por Responder "x"

#Bienvenida a la TRIVIA
print(
    "Pruba tus conocimientos resolviendo estas siemples preguntas \nde cultura general de nuestra TRIVIA y conoce tu nivel. \n"
)
#--Ingresa el nombre del participante 
participante = input("Escribe tu nombre:")
#--variable para el puntaje
puntaje = 0
print("\n")

#INSTRUCCIONES
print(
    "Bienvenido", participante,
    "! Escribe la letra que consideres correcta y presiona \nEnter para enviar la respuesta \n"
)
print("Tu puntaje actual es de:", puntaje, "\n")

#Pregunta 1-----------------------------------------------
print("1)¿Cual es el RIO mas largo del mundo? \n")
print("a) Río Nilo")
print("b) Río Amazonas")
print("c) Río Congue")
print("d) Río Misisipi")

respuesta_1 = input("\nRESPUESTA: ")

#Condicional:
#--Es necesario colocar una respuesta para continuar
while respuesta_1 not in ("a", "b", "c", "d","x"):
    respuesta_1 = input("Coloque una respuesta:")
#--Condicional para mostrar un msj segun su respuesta
if respuesta_1 == "b":
  #--Se le aumenta 10 puntos si es correcto
    puntaje += random.randint(0, 3) + 10
    print("Excelente", participante, "respuesta correcta!")
    print("¿Sabías que? mide 6992 km de longitud\n")
#--Msj secreto
elif respuesta_1 == "x":
    puntaje += 5
    print(participante, "Este es un mensaje secreto! No le digas a nadie que ganaste 5 puntos\n")
  
else:
  #--Se le resta 5 puntos si se equivoca 
    puntaje -= random.randint(0, 3) + 5
    print("Lo sentimos", participante, "Respuesta Incorrecta!\n")
#--mostrar el puntaje por pregunta resuelta
print("Puntos:", puntaje)
print("\n")

#Pregunta 2---------------------------------------------
print("2)¿Cúal es el pais con más habitantes del mundo? \n")
print("a) Rusia")
print("b) EEUU")
print("c) China")
print("d) La India")

respuesta_2 = input("\nRESPUESTA: ")

#Condicional:
while respuesta_2 not in ("a", "b", "c", "d", "x"):
    respuesta_2 -= input(
        "Debes responder unas de las alternativas; a, b, c, d. Ingresa nuevamente tu respuesta"
    )

if respuesta_2 == "a":
    puntaje -= random.randint(0, 5) + 5
    print("Incorrecto", participante,
          "Rusia tiene 142 mil habitantes aproximadamente\n")

elif respuesta_2 == "b":
    puntaje -= random.randint(0, 5) + 5
    print("Incorrecto", participante,
          "EEUU tiene 337 mil habitantes aproximadamente\n")

elif respuesta_2 == "d":
    puntaje -= random.randint(0, 5) + 5
    print("Incorrecto", participante,
          "La India tiene 1.389 millones de habitantes aproximadamente\n")

elif respuesta_2 == "x":
    puntaje += 5
    print(participante, "Este es un mensaje secreto! No le digas a nadie que ganaste 5 puntos\n")
    
else:
    puntaje += random.randint(0, 5) + 10
    print(
        "Excelente", participante,
        "¿Sabías que? China cuenta con 1.412 millones de habitanes aproximadamente\n"
    )

print("Puntos:", puntaje)
print("\n")

#Pregunta 3----------------------------------------------
print("Pregunta con puntos especiales\n")
print("3)¿Cuantos años duró la segunda guerra mundial? \n")
print("a) 10 años")
print("b) 8 años")
print("c) 5 años")
print("d) 6 años")

respuesta_3 = input("\nRESPUESTA: ")

#Condicional:
while respuesta_3 not in ("a", "b", "c", "d","x"):
    respuesta_3 = input("Coloque una respuesta:")

if respuesta_3 == "a":
  puntaje -= random.randint(0, 7) + 5
  puntaje = puntaje / 2 
  print("Lo sentimos", participante, "Respuesta Totalmente Incorrecta!\n")

if respuesta_3 == "b":
  puntaje -= random.randint(0, 7) + 5
  puntaje = puntaje - 5
  print("Lo sentimos", participante, "Respuesta Incorrecta!\n")

if respuesta_3 == "c":
  puntaje -= random.randint(0, 7) + 5
  puntaje = puntaje + 5
  print("Lo sentimos", participante, "Respuesta Incorrecta! pero estuviste cerca\n")

elif respuesta_3 == "x":
    puntaje += 5
    print(participante, "Este es un mensaje secreto! No le digas a nadie que ganaste 5 puntos\n")

else:
    puntaje += random.randint(0, 7) + 10
    puntaje = puntaje * 2
    print("Excelente", participante, "respuesta correcta!")
    print(
        "¿Sabías que? Terminó en el año 1945 en 2 de septiembre con la firma oficial de rendición por parte de Japón"
    )
    

print("Puntos:", puntaje)
print("\n")

#pregunta 4 ------------------------------------------------
print("4)¿Cúal fué el primer telefono inteligente en salir a la venta? \n")
print("a) Ericsson GS88")
print("b) Siemens S10")
print("c) BlackBerry 5810")
print("d) Nokia 9000 Communicator")

respuesta_4 = input("\nRESPUESTA: ")

#Condicional:
while respuesta_4 not in ("a", "b", "c", "d","x"):
    respuesta_4 = input("Coloque una respuesta:")

if respuesta_4 == "d":
    puntaje += random.randint(0, 10) + 10
    print("Excelente", participante, "respuesta correcta!")
    print(
        "¿Sabías que? Se presentó el 15 de aagosto de 1996 en una fería en Alemanía\n"
    )
elif respuesta_4 == "x":
    puntaje += 5
    print(participante, "Este es un mensaje secreto! No le digas a nadie que ganaste 5 puntos\n")

else:
    puntaje -= random.randint(0, 10) + 10
    print("Lo sentimos", participante, "Respuesta Incorrecta!\n")

print("Puntos:", puntaje)
print("\n")


#--Condicional para mostrar msj deacuerdo a los puntos obtenidos
if puntaje < 0:
    print("Gracias por participar", participante,
          "a lo mejor deberias estudiar un poco mas. Debes", puntaje, "puntos")

elif puntaje <= 25:
    print("Gracias por participar", participante,
          "Esta bien para comenzar, obtuviste", puntaje, "puntos")

else:
    print("Gracias por participar", participante,
          "Lo hiciste estupendo, tu puntaje es:", puntaje, "puntos")

