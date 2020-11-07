import turtle
import time
import random

wait = 0.1

#Marcador
score = 0
high_score = 0

#Configuracion de la Ventana
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("#212121")
wn.setup(width=600,height=600)
wn.tracer(0)

#Crear cabeza de serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("#F7F7F7")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Crear comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("#CF0000")
comida.penup()
comida.goto(0,100)

#Cuerpo serpiente
partes = []

#Crear marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("#DF8729")
marcador.penup()
marcador.hideturtle()
marcador.goto(0,260)
marcador.write("Score: 0       High Score: 0", align = "center", font=("Courier",22,"bold"))

#Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def derecha():
    cabeza.direction = "right"
def izquierda():
    cabeza.direction = "left"

def movimiento():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y+20)
    
    elif cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y-20)
    
    elif cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x+20)
    
    elif cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x-20)

#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(derecha, "Right")
wn.onkeypress(izquierda, "Left")

wn.onkeypress(arriba, "w")
wn.onkeypress(abajo, "s")
wn.onkeypress(derecha, "d")
wn.onkeypress(izquierda, "a")

#Mainloop

while True:
    wn.update()

    #Colisiones de borde
    if cabeza.xcor() > 280 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #Esconder las partes
        for parte in partes:
            parte.goto(1000,1000)

        #Limpiar la lista de partes
        partes.clear()

        #Resetear marcador
        score = 0
        marcador.clear()
        marcador.write(f"Score: {score}      High Score: {high_score}", align = "center", font=("Courier",22,"bold"))
        

    #Colisión con comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        nueva_parte = turtle.Turtle()
        nueva_parte.speed(0)
        nueva_parte.shape("square")
        nueva_parte.color("#CBCBCB")
        nueva_parte.penup()
        partes.append(nueva_parte)
        
        #Aumentar marcador

        score += 10

        #Ingresar High Score

        if score > high_score:
            high_score = score

        marcador.clear()
        marcador.write(f"Score: {score}      High Score: {high_score}", align = "center", font=("Courier",22,"bold"))

    #Mover el cuerpo de la serpiente
    totalSeg = len(partes)
    for i in range(totalSeg-1,0,-1):
        x = partes[i-1].xcor()
        y = partes[i-1].ycor()
        partes[i].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        partes[0].goto(x,y)

    movimiento()

    #Colisiones con el cuerpo
    for parte in partes:
        if parte.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            #Esconder los segmentos
            for parte in partes:
                parte.goto(1000,1000)
            
            #Limpiar la lista
            partes.clear()

            #Resetear marcador
            score = 0
            marcador.clear()
            marcador.write(f"Score: {score}      High Score: {high_score}", align = "center", font=("Courier",22,"bold"))

    time.sleep(wait)