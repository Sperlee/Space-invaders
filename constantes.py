from PPlay.window import *
from PPlay.gameimage import GameImage
from PPlay.sprite import *

#Definições básicas:
janela = Window (1280, 720)
mouse = Window.get_mouse()
teclado = Window.get_keyboard()
janela.set_title("Star Pixel")

#GameImages:
cenario = GameImage("fundo.jpg")


#GameImages dos botões:
botaoplay = GameImage("play.png")
botaodif = GameImage("dificuldade.png")
botaorank = GameImage("rank.png")
botaoexit = GameImage("sair.png")
botaofacil = GameImage("facil.png")
botaomedio = GameImage("medio.png")
botaodificil = GameImage("dificil.png")
botaoback = GameImage("back.png")

#botoes menu principal
botaoplay.x = botaoplay.width - 20
botaoplay.y = botaoplay.height
botaodif.x = botaodif.width - 150
botaodif.y = botaodif.height + 100
botaorank.x = botaorank.width - 77
botaorank.y = botaorank.height + 200
botaoexit.x = janela.width - 100
botaoexit.y = janela.height - 100

#dificuldades
botaofacil.x = janela.width/3 - botaofacil.width/2
botaofacil.y = janela.height/2
botaomedio.x = janela.width/2 - botaomedio.width/2
botaomedio.y = janela.height/2
botaodificil.x = janela.width/1.5-botaodificil.width/2
botaodificil.y = janela.height/2

#botão back
botaoback.x = janela.width/2 - botaoback.width/2
botaoback.y = janela.height - botaoback.height


Nave = GameImage("botao.png")
vel_nave = 500
Nave.x = janela.width/2 - Nave.width/2
Nave.y = janela.height - Nave.height
life_Nave = 3
vida = [GameImage("vida.png"),GameImage("vida.png"),GameImage("vida.png")]

K = 1
tiro_delay = 0.5
tiro = []


nome = ""
pontos = 0


inimigos = [[GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png")],[GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png")],[GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png")],[GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png")],[GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png")]]
inimigos_linha = [GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png")]
distancia_inimigos = inimigos[0][0].width
posição_inimigos = 10
velocidade_inimigo = 1
coluna = 5
linha = 3

for i in range(linha):
    for j in range(coluna):
        if (inimigos[i][j] != 0):
            inimigos[i][j].x = j * (posição_inimigos + 100) + janela.width / 3
            inimigos[i][j].y = i * (posição_inimigos + 100) + posição_inimigos




def resetar(inimigos):
    inimigos = [
        [GameImage("inimigos.png"), GameImage("inimigos.png"), GameImage("inimigos.png"), GameImage("inimigos.png"),
         GameImage("inimigos.png")],
        [GameImage("inimigos.png"), GameImage("inimigos.png"), GameImage("inimigos.png"), GameImage("inimigos.png"),
         GameImage("inimigos.png")],
        [GameImage("inimigos.png"), GameImage("inimigos.png"), GameImage("inimigos.png"), GameImage("inimigos.png"),
         GameImage("inimigos.png")]]
    
tiro_inimigo = []
vel_tiro_inimigo = 1
delay_inimigo = 0
tempo_delay = 0.5

fps = 0
fpstext = 0
contador = 0
fpsletra = 'FPS:'

morto = False
contador_time = 0

animação = Sprite("sprite_nave.png",4)
animação.set_total_duration(100)