from PPlay.window import *
from PPlay.gameimage import GameImage

#Definições básicas:
janela = Window (1280, 720)
mouse = Window.get_mouse()
teclado = Window.get_keyboard()
janela.set_title("Star Pixel")

#GameImages:
cenario = GameImage("fundo.jpg")


#GameImages dos botões:
botaoplay = GameImage("botao.png")
botaodif = GameImage("botao.png")
botaorank = GameImage("botao.png")
botaoexit = GameImage("botao.png")
botaofacil = GameImage("botao.png")
botaomedio = GameImage("botao.png")
botaodificil = GameImage("botao.png")
botaoback = GameImage("botao.png")


botaoplay.x = janela.width/3 - botaoplay.width/2
botaoplay.y = janela.height/2
botaodif.x = janela.width - janela.width/3 - botaodif.width/2
botaodif.y = janela.height/2
botaorank.x = janela.width/3 - botaodif.width/2
botaorank.y = janela.height/2 + 150
botaoexit.x = janela.width - janela.width/3 - botaodif.width/2
botaoexit.y = janela.height/2 + 150
botaofacil.x = janela.width/3 - botaofacil.width
botaofacil.y = janela.height/2
botaomedio.x = janela.width/2 - botaomedio.width/2
botaomedio.y = janela.height/2
botaodificil.x = janela.width/2 + botaodificil.width
botaodificil.y = janela.height/2
botaoback.x = janela.width/2 - botaoback.width/2
botaoback.y = janela.height - botaoback.height


Nave = GameImage("botao.png")
vel_nave = 500
Nave.x = janela.width/2 - Nave.width/2
Nave.y = janela.height - Nave.height

K = 0
tiro_delay = 0.3
tiro = []
pontos = 0


inimigos = [[GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png")],[GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png")],[GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png"),GameImage("inimigos.png")]]

distancia_inimigos = inimigos[0][0].width
posição_inimigos = 10
velocidade_inimigo = 1

for i in range(3):
    for j in range(5):
        if (inimigos[i][j] != 0):
            inimigos[i][j].x = j * (posição_inimigos + 100) + janela.width / 3
            inimigos[i][j].y = i * (posição_inimigos + 100) + posição_inimigos


dificuldade = 1


def resetar(inimigos):
    inimigos = [
        [GameImage("inimigos.png"), GameImage("inimigos.png"), GameImage("inimigos.png"), GameImage("inimigos.png"),
         GameImage("inimigos.png")],
        [GameImage("inimigos.png"), GameImage("inimigos.png"), GameImage("inimigos.png"), GameImage("inimigos.png"),
         GameImage("inimigos.png")],
        [GameImage("inimigos.png"), GameImage("inimigos.png"), GameImage("inimigos.png"), GameImage("inimigos.png"),
         GameImage("inimigos.png")]]
    



fps = 0
fpstext = 0
contador = 0
fpsletra = 'FPS:'
