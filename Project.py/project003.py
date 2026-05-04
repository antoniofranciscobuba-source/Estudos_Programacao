from turtle import *
from colorsys import *

# 1. Configurações de Performance e Tela
setup(1200, 700)  # Tela larga para caber o desenho e o nome
speed(0)
bgcolor("black")
hideturtle()
tracer(0) # Desenha instantaneamente

def desenhar_mandala():
    h = 0
    penup()
    goto(-300, 0) # Move a mandala para a ESQUERDA
    pendown()
    
    for i in range(100):
        color(hsv_to_rgb(h, 1, 1))
        # Desenha a forma da mandala
        forward(i * 2)
        left(91)
        h += 0.01
    update()

def escrever_nome_lateral():
    penup()
    # Move para a DIREITA para escrever o nome
    goto(200, -50) 
    color("white")
    
    # Escreve o nome bem grande e elegante
    write("GRACE", align="left", font=("Arial", 120, "bold italic"))
    
    # Linha decorativa embaixo do nome
    goto(210, -70)
    pendown()
    pensize(5)
    forward(450)
    update()

def mensagem_boas_vindas():
    penup()
    goto(0, -300)
    color("gray")
    write("BEM-VINDA À FRANÇA 🇫🇷", align="center", font=("Arial", 25, "normal"))
    update()

# Executando as funções
print("[LOG] Criando o presente da Grace...")
desenhar_mandala()
escrever_nome_lateral()
mensagem_boas_vindas()
done()