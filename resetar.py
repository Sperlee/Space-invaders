import constantes
from PPlay.gameimage import GameImage
import random
def reset():
    for i in range(constantes.linha):
        for j in range(constantes.coluna):
            constantes.inimigos[i][j] = GameImage("inimigos.png")

    for i in range(constantes.linha):
        for j in range(constantes.coluna):
            if (constantes.inimigos[i][j] != 0):
                constantes.inimigos[i][j].x = j * (constantes.posição_inimigos + 100) + constantes.janela.width / 3
                constantes.inimigos[i][j].y = i * (constantes.posição_inimigos + 100) + constantes.posição_inimigos


def prox(C):
    for i in range(C):
        for j in range(constantes.coluna):
            constantes.inimigos[i][j] = GameImage("inimigos.png")

    for i in range(C):
        for j in range(constantes.coluna):
            if (constantes.inimigos[i][j] != 0):
                constantes.inimigos[i][j].x = j * (constantes.posição_inimigos + 100) + constantes.janela.width / 3
                constantes.inimigos[i][j].y = i * (constantes.posição_inimigos + 100) + constantes.posição_inimigos


def resetar_pontos():
    constantes.Nave.x = constantes.janela.width/2 - constantes.Nave.width/2
    constantes.Nave.y = constantes.janela.height - constantes.Nave.height
    constantes.pontos = 0
    constantes.life_Nave = 3
    constantes.tiro_inimigo = []
    constantes.tiro = []
    constantes.linha = 3