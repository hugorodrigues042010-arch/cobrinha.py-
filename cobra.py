import turtle
import time
import random

atraso = 0.1
pontuacao = 0
recorde = 0

# Configuração da Janela
janela = turtle.Screen()
janela.title("Jogo da Cobrinha (Snake)")
janela.bgcolor("black")
janela.setup(width=600, height=600)
janela.tracer(0)

# Cabeça da cobra
cabeca = turtle.Turtle()
cabeca.speed(0)
cabeca.shape("square")
cabeca.color("green")
cabeca.penup()
cabeca.goto(0, 0)
cabeca.direcao = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

corpo = []

# Placar
placar = turtle.Turtle()
placar.speed(0)
placar.shape("square")
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write("Pontos: 0  Recorde: 0", align="center", font=("Courier", 18, "normal"))

# Controlos
def subir():
    if cabeca.direcao != "down":
        cabeca.direcao = "up"

def descer():
    if cabeca.direcao != "up":
        cabeca.direcao = "down"

def esquerda():
    if cabeca.direcao != "right":
        cabeca.direcao = "left"

def direita():
    if cabeca.direcao != "left":
        cabeca.direcao = "right"

def mover():
    if cabeca.direcao == "up":
        y = cabeca.ycor()
        cabeca.sety(y + 20)

    if cabeca.direcao == "down":
        y = cabeca.ycor()
        cabeca.sety(y - 20)

    if cabeca.direcao == "left":
        x = cabeca.xcor()
        cabeca.setx(x - 20)

    if cabeca.direcao == "right":
        x = cabeca.xcor()
        cabeca.setx(x + 20)

# Mapeamento do teclado
janela.listen()
janela.onkeypress(subir, "Up")
janela.onkeypress(descer, "Down")
janela.onkeypress(esquerda, "Left")
janela.onkeypress(direita, "Right")

# Loop principal do jogo
while True:
    janela.update()

    # Colisão com os limites da tela
    if cabeca.xcor() > 290 or cabeca.xcor() < -290 or cabeca.ycor() > 290 or cabeca.ycor() < -290:
        time.sleep(1)
        cabeca.goto(0, 0)
        cabeca.direcao = "stop"

        for segmento in corpo:
            segmento.goto(1000, 1000)
        corpo.clear()

        pontuacao = 0
        placar.clear()
        placar.write(f"Pontos: {pontuacao}  Recorde: {recorde}", align="center", font=("Courier", 18, "normal"))

    # Colisão com a comida
    if cabeca.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        novo_segmento = turtle.Turtle()
        novo_segmento.speed(0)
        novo_segmento.shape("square")
        novo_segmento.color("lightgreen")
        novo_segmento.penup()
        corpo.append(novo_segmento)

        pontuacao += 10
        if pontuacao > recorde:
            recorde = pontuacao

        placar.clear()
        placar.write(f"Pontos: {pontuacao}  Recorde: {recorde}", align="center", font=("Courier", 18, "normal"))

    # Mover os segmentos do corpo
    for i in range(len(corpo) - 1, 0, -1):
        x = corpo[i - 1].xcor()
        y = corpo[i - 1].ycor()
        corpo[i].goto(x, y)

    if len(corpo) > 0:
        x = cabeca.xcor()
        y = cabeca.ycor()
        corpo[0].goto(x, y)

    mover()

    # Colisão com o próprio corpo
    for segmento in corpo:
        if segmento.distance(cabeca) < 20:
            time.sleep(1)
            cabeca.goto(0, 0)
            cabeca.direcao = "stop"

            for seg in corpo:
                seg.goto(1000, 1000)
            corpo.clear()

            pontuacao = 0
            placar.clear()
            placar.write(f"Pontos: {pontuacao}  Recorde: {recorde}", align="center", font=("Courier", 18, "normal"))

    time.sleep(atraso)