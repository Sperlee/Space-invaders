import constantes
from PPlay.gameimage import GameImage

def reset():
    constantes.pontos = 0
    constantes.Nave.x = constantes.janela.width/2 - constantes.Nave.width/2
    constantes.Nave.y = constantes.janela.height - constantes.Nave.height

    for i in range(3):
        for j in range(5):
            constantes.inimigos[i][j] = GameImage("inimigos.png")

    for i in range(3):
        for j in range(5):
            if (constantes.inimigos[i][j] != 0):
                constantes.inimigos[i][j].x = j * (constantes.posição_inimigos + 100) + constantes.janela.width / 3
                constantes.inimigos[i][j].y = i * (constantes.posição_inimigos + 100) + constantes.posição_inimigos