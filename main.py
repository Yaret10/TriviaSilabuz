import random
import time
import os


# +5 puntos por Responder "x"
#--------variables a usar----
#colores
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
#----------------
puntaje = 0 #Almacena puntaje
iniciar_trivia = True #Almacena estado de trivia
intentos_trivia = 0 #Almacena cauntos intentos lleva la trivia 

#--Bienvenida a la TRIVIA
print(
    GREEN+"Pruba tus conocimientos resolviendo estas siemples preguntas \nde cultura general de nuestra TRIVIA y conoce tu nivel. \n"+RESET
)
#--Ingresa el nombre del participante 
participante = input("Escribe tu nombre:")
print("\n")

#--INSTRUCCIONES 
print(
    "Bienvenido"+CYAN, participante,RESET+
    "! Escribe la letra que consideres correcta y presiona \nEnter para enviar la respuesta \n"
)
print(MAGENTA+"Tu puntaje actual es de:", puntaje, "\n"+RESET)


print("Reglamento de la trivia:")
print("  1ra pregunta") 
print("    RCorrect = 10 puntos + (0,3) puntos aleatorios")
print("    RIncorrect = -(5 puntos + (0,3) puntos aleatorios)")
print("  2da pregunta")
print("    RCorrect = 10 puntos + (0,5) puntos aleatorios")
print("    RIncorrect = -(5 puntos + (0,5) puntos aleatorios)")
print("  3da pregunta")
print("    RCorrect = 10 puntos + (0,7) puntos aleatorios")
print("    RIncorrect = -(5 puntos + (0,7) puntos aleatorios)")
print("  4da pregunta")
print("    RCorrect = 10 puntos + (0,10) puntos aleatorios")
print("    RIncorrect = -(5 puntos + (0,10) puntos aleatorios)")
print(RED+"--Hay una respuesta con puntos Bonus, averigualo con tu eXperiencia-- :)"+RESET)

input("\nPresiona enter para empezar!\n")
os.system('clear') #Limpiar Pantalla


#--funcion para el for(tiempo de carga antes de empezar)
def tiempoCarga():
  print("Empezamos en...")
  for x in range(5,0,-1):
    print(x)
    time.sleep(1)
tiempoCarga()
print("\n")

os.system('clear') #Limpiar pantalla

#Trivia-----
while iniciar_trivia == True:
  intentos_trivia +=1
  puntaje = 0
  
  print("Intento Nro: ",intentos_trivia,"\n")
  
  #Pregunta 1-----------------------------------------------
  print(GREEN+"1)¿Cual es el RIO mas largo del mundo? \n"+RESET)
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
      print(BLUE+"Excelente", participante, "respuesta correcta!")
      print("¿Sabías que? mide 6992 km de longitud\n"+RESET)
  #--Msj secreto
  elif respuesta_1 == "x":
      puntaje += 5
      print(participante, "Este es un mensaje secreto! No le digas a nadie que ganaste 5 puntos\n") 
  #Respuesta Incorrecta
  else:
    #--Se le resta 5 puntos si se equivoca 
      puntaje -= random.randint(0, 3) + 5
      print(RED+"Lo sentimos", participante, "Respuesta Incorrecta!\n"+RESET) 
    
  print(MAGENTA+"Puntos:", puntaje,RESET) #Muestra puntaje
  print("\n")
  #----tiempo de espera
  time.sleep(2)
  
  
  #Pregunta 2---------------------------------------------
  print(GREEN+"2)¿Cúal es el pais con más habitantes del mundo? \n"+RESET)
  print("a) Rusia")
  print("b) EEUU")
  print("c) China")
  print("d) La India")
  
  respuesta_2 = input("\nRESPUESTA: ")
  
  #Condicional:
  while respuesta_2 not in ("a", "b", "c", "d", "x"):

    if respuesta_2 == "":
        respuesta_2 = input("Coloque una respuesta: ")
    else:
        respuesta_2 = input(
          "Debes responder unas de las alternativas; a, b, c, d. Ingresa nuevamente tu respuesta: "
      )
  #Respuesta Incorrecta
  if respuesta_2 == "a":
      puntaje -= random.randint(0, 5) + 5
      print(RED+"Incorrecto", participante,
            "Rusia tiene 142 mil habitantes aproximadamente\n"+RESET)
  
  elif respuesta_2 == "b":
      puntaje -= random.randint(0, 5) + 5
      print(RED+"Incorrecto", participante,
            "EEUU tiene 337 mil habitantes aproximadamente\n"+RESET)
  
  elif respuesta_2 == "d":
      puntaje -= random.randint(0, 5) + 5
      print(RED+"Incorrecto", participante,
            "La India tiene 1.389 millones de habitantes aproximadamente\n"+RESET)
  
  elif respuesta_2 == "x":
      puntaje += 5
      print(participante, "Este es un mensaje secreto! No le digas a nadie que ganaste 5 puntos\n")
    
  #Respuesta Correcta
  else:
      puntaje += random.randint(0, 5) + 10
      print(
          BLUE+"Excelente", participante,
          "¿Sabías que? China cuenta con 1.412 millones de habitanes aproximadamente\n"+RESET
      )
  
  print(MAGENTA+"Puntos:", puntaje,RESET) #Muestra puntaje
  print("\n")
  #----tiempo de espera
  time.sleep(2)
  
  #Pregunta 3----------------------------------------------
  print(GREEN+"Pregunta con puntos especiales\n")
  print("3)¿Cuantos años duró la segunda guerra mundial? \n"+RESET)
  print("a) 10 años")
  print("b) 8 años")
  print("c) 5 años")
  print("d) 6 años")
  
  respuesta_3 = input("\nRESPUESTA: ")
  
  #Condicional:
  while respuesta_3 not in ("a", "b", "c", "d","x"):
      respuesta_3 = input("Coloque una respuesta:")
  #Respuesta Incorrecta
  if respuesta_3 == "a":
    puntaje -= random.randint(0, 7) + 5
    puntaje = puntaje / 2 
    print(RED+"Lo sentimos", participante, "Respuesta Totalmente Incorrecta!\n"+RESET)
  
  elif respuesta_3 == "b":
    puntaje -= random.randint(0, 7) + 5
    puntaje = puntaje - 5
    print(RED+"Lo sentimos", participante, "Respuesta Incorrecta!\n"+RESET)
  
  elif respuesta_3 == "c":
    puntaje -= random.randint(0, 7) + 5
    puntaje = puntaje + 5
    print(RED+"Lo sentimos", participante, "Respuesta Incorrecta! pero estuviste cerca\n"+RESET)
  
  elif respuesta_3 == "x":
      puntaje += 5
      print(participante, "Este es un mensaje secreto! No le digas a nadie que ganaste 5 puntos\n")
  #Respuesta correcta
  else:
      puntaje += random.randint(0, 7) + 10
      puntaje = puntaje * 2
      print(BLUE+"Excelente", participante, "respuesta correcta!")
      print(
          "¿Sabías que? Terminó en el año 1945 en 2 de septiembre con la firma oficial de rendición por parte de Japón \n"+RESET
      )
      
  
  print(MAGENTA+"Puntos:", puntaje,RESET) #Mostrar puntaje 
  print("\n")
  #----tiempo de espera
  time.sleep(2)
  
  #pregunta 4 ------------------------------------------------
  print(GREEN+"4)¿Cúal fué el primer telefono inteligente en salir a la venta? \n"+RESET)
  print("a) Ericsson GS88")
  print("b) Siemens S10")
  print("c) BlackBerry 5810")
  print("d) Nokia 9000 Communicator")
  
  respuesta_4 = input("\nRESPUESTA: ")
  
  #Condicional:
  while respuesta_4 not in ("a", "b", "c", "d","x"):
      respuesta_4 = input("Coloque una respuesta:")
    
  #Respuesta correcta
  if respuesta_4 == "d":
      puntaje += random.randint(0, 10) + 10
      print(BLUE+"Excelente", participante, "respuesta correcta!")
      print(
          "¿Sabías que? Se presentó el 15 de aagosto de 1996 en una fería en Alemanía\n"+RESET
      )
  #Mensaje secreto
  elif respuesta_4 == "x":
      puntaje += 5
      print(participante, "Este es un mensaje secreto! No le digas a nadie que ganaste 5 puntos\n")
  
  #Respuesta incorrecta
  else:
      puntaje -= random.randint(0, 10) + 10
      print(RED+"Lo sentimos", participante, "Respuesta Incorrecta!\n"+RESET)
  
  print(MAGENTA+"Puntos:", puntaje,RESET) #Muestra puntaje 
  print("\n")
  #----tiempo de espera
  time.sleep(2)

#--------Condicional para mostrar msj deacuerdo a los puntos obtenidos-------------
  if puntaje < 0:
      print("Gracias por participar", participante,
            "a lo mejor deberias estudiar un poco mas. Debes", puntaje, "puntos")
  
  elif puntaje <= 25:
      print("Gracias por participar", participante,
            "Esta bien para comenzar, obtuviste", puntaje, "puntos")
  
  else:
      print("Gracias por participar"+CYAN, participante,RESET+
            "Lo hiciste estupendo, tu puntaje es:"+MAGENTA, puntaje, "puntos"+RESET)
#------------------------------Fin del While-----------------------
  repetir_trivia = input(YELLOW+"\n Deseas Intentar la Trivia nuevamente?. Escribe si para continuar o cualquier letra para finalizar:"+RESET+"\n").lower()
  
  if repetir_trivia != "si":
    print("\n Gracias por participar estimado",participante,", Hasta pronto!")
    iniciar_trivia = False
  else:
    os.system('clear')


