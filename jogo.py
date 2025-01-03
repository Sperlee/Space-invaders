from PPlay.collision import Collision
from constantes import*
import constantes
from PPlay.gameimage import GameImage
import inicio
import resetar
import random
import rank
from PPlay.sprite import *


def tela_do_jogo(mouse,teclado,dificuldade):
    cenario.draw()
    #movimentação da Nave
    if(constantes.morto == True):
        constantes.contador_time += janela.delta_time()
        constantes.Nave.x = janela.width/2
        constantes.Nave.y = janela.height - 75
        animação.x = janela.width/2
        animação.y = janela.height - 75
        if(constantes.contador_time >= 1):
            constantes.morto = False
            constantes.contador_time = 0
    if(teclado.key_pressed("right") and Nave.x <= janela.width - Nave.width):
        Nave.x += vel_nave * (janela.delta_time())
    if(teclado.key_pressed("left") and Nave.x >= 0):
        Nave.x -= vel_nave * (janela.delta_time())


    #disparo da Nave
    if(constantes.morto == False):
        if(teclado.key_pressed("space")):
            if constantes.K*(1/((dificuldade)**1/2)) >  constantes.tiro_delay:
                munição = GameImage("tiro.png")
                munição.x = Nave.x + 20
                munição.y = janela.height - Nave.height - munição.height
                tiro.append(munição)
                constantes.K = 0



    # colisão do tiro
    for i in range(constantes.linha-1,-1,-1):
        for j in range(coluna-1,-1,-1):
            if inimigos[i][j] != 0:
                inimigos[i][j].draw()
                for k in tiro:
                    if inimigos[i][j] != 0:
                        if inimigos[i][j].collided(k):
                            inimigos[i][j] = 0
                            tiro.remove(k)
                            constantes.pontos += int(10*dificuldade*(100*janela.delta_time()))



    #colisão nas paredes
    for i in range(constantes.linha-1,-1,-1):
        for j in range(coluna-1,-1,-1):
            if inimigos[i][j] != 0:
                inimigos[i][j].x +=constantes.velocidade_inimigo
                if inimigos[i][j].x >= janela.width - inimigos[i][j].width or inimigos[i][j].x <= 0:
                    constantes.velocidade_inimigo = -1 * constantes.velocidade_inimigo
                    for x in range(constantes.linha-1,-1,-1):
                        for y in range(coluna-1,-1,-1):
                            if inimigos[x][y] != 0:
                                inimigos[x][y].y += dificuldade * 40
                                if inimigos[x][y].y >= Nave.y - 25:
                                    constantes.nome = str(input("Insira seu Nome: "))
                                    rank.adicionar_pontuacao(constantes.nome,constantes.pontos)
                                    resetar.reset()
                                    resetar.resetar_pontos()
                                    inicio.Menu(janela,mouse,teclado)



    #tiro inimigo
    if(constantes.delay_inimigo*(dificuldade)**(1/2) > constantes.tempo_delay):                              
        X = random.randint(0,constantes.linha-1)
        Y = random.randint(0,coluna-1)
        for i in range(constantes.linha-1,-1,-1):
            for j in range(coluna-1,-1,-1):
                if(inimigos[i][j] != 0):
                    if(X == i and Y == j):
                        tiro_inimigo.append(GameImage("tiro.png"))
                        tiro_inimigo[len(tiro_inimigo)-1].x = inimigos[i][j].x
                        tiro_inimigo[len(tiro_inimigo)-1].y = inimigos[i][j].y
        constantes.delay_inimigo = 0
    for i in range(len(tiro_inimigo)):
        if(tiro_inimigo[i] != 0):
            tiro_inimigo[i].draw()
            tiro_inimigo[i].y += dificuldade*1.3*constantes.vel_tiro_inimigo
            if(constantes.morto == False):
                if(Nave.collided(tiro_inimigo[i])):
                    constantes.life_Nave -= 1
                    tiro_inimigo[i] = 0
                    constantes.morto = True
        if(constantes.life_Nave == 0):
            constantes.nome = str(input("Insira seu Nome: "))
            rank.adicionar_pontuacao(constantes.nome,constantes.pontos)
            resetar.reset()
            resetar.resetar_pontos()
            inicio.Menu(janela,mouse,teclado)



    conferir = True
    #teste de 0 inimigos
    for i in range(linha):
        if(conferir == False):
            break
        for j in range(coluna):
            if(inimigos[i][j] != 0):
                conferir = False
                break
    if(conferir == True):
        if(constantes.linha < 4):
            constantes.linha += 1
            resetar.prox(constantes.linha)
            constantes.vel_tiro_inimigo += 1/dificuldade
        else:
            constantes.vel_tiro_inimigo +=1/dificuldade
            resetar.reset()
    
    if constantes.fps < 1:
        constantes.fps += janela.delta_time()
        constantes.contador += 1 
    else:
        constantes.fpstext = constantes.contador 
        constantes.contador, constantes.fps = 0, 0 



    #DRAWS
    for i in range(constantes.life_Nave):
        constantes.vida[i].x = janela.width - (i+1)*50
        constantes.vida[i].y = constantes.vida[i].height
        vida[i].draw()
    janela.draw_text(f"FPS: {constantes.fpstext}", 60, 10, size=20, color=(255, 255, 255),
                 font_name="Arial", bold=True, italic=False)

    janela.draw_text(f"Pontos:{int(constantes.pontos)}",janela.width - 150,janela.height - 50,size=20, color=(255, 255, 255),
                 font_name="Arial", bold=True, italic=False)

    for i in tiro:
        i.y -= 5
        if (i.y < 0):
            tiro.remove(i)
    for i in range(len (tiro)):
        tiro[i].draw()
    if(constantes.morto == False):
        constantes.Nave.draw()
    if(constantes.morto == True):
        animação.draw()
        animação.update()

    #constantes para delay
    constantes.K += janela.delta_time()
    constantes.delay_inimigo += janela.delta_time()