from PPlay.collision import Collision
from constantes import*
import constantes
from PPlay.gameimage import GameImage
import inicio
import resetar

def tela_do_jogo(mouse,teclado):
    cenario.draw()
    if(teclado.key_pressed("right") and Nave.x <= janela.width - Nave.width):
        Nave.x += vel_nave * (janela.delta_time())
    if(teclado.key_pressed("left") and Nave.x >= 0):
        Nave.x -= vel_nave * (janela.delta_time())

    if(teclado.key_pressed("space")):
        if constantes.K >  constantes.tiro_delay:
            munição = GameImage("tiro.png")
            munição.x = Nave.x + 20
            munição.y = janela.height - Nave.height - munição.height
            tiro.append(munição)
            constantes.K = 0

    # Adicione uma flag para verificar se o jogo deve ser reiniciado
    reiniciar_jogo = False

    for i in range(3):
        for j in range(5):
            if inimigos[i][j] != 0:
                inimigos[i][j].draw()
                for k in tiro:
                    if inimigos[i][j] != 0:
                        if inimigos[i][j].collided(k):
                            inimigos[i][j] = 0
                            tiro.remove(k)

    for i in range(3):
        for j in range(5):
            if inimigos[i][j] != 0:
                inimigos[i][j].x += constantes.velocidade_inimigo
                if inimigos[i][j].x >= janela.width - inimigos[i][j].width or inimigos[i][j].x <= 0:
                    constantes.velocidade_inimigo = -1 * constantes.velocidade_inimigo
                    for x in range(3):
                        for y in range(5):
                            if inimigos[x][y] != 0:
                                inimigos[x][y].y += 100
                                if inimigos[x][y].y >= Nave.y:
                                    resetar.reset()
                                    inicio.Menu(janela,mouse,teclado)

    
    if constantes.fps < 1:
        constantes.fps += janela.delta_time()
        constantes.contador += 1 
    else:
        constantes.fpstext = constantes.contador 
        constantes.contador, constantes.fps = 0, 0 

    janela.draw_text(f"FPS: {constantes.fpstext}", 60, 10, size=20, color=(255, 255, 255),
                 font_name="Arial", bold=True, italic=False)



    for i in tiro:
        i.y -= 5
        if (i.y < 0):
            tiro.remove(i)
    constantes.K += janela.delta_time()
    for i in range(len (tiro)):
        tiro[i].draw()
    Nave.draw()
