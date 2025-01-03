import constantes
import jogo
from constantes import*
import resetar
import rank

#Função Menu:
def Menu (janela,mouse,teclado):
    #Variáveis condicionais:
    menu = True
    dificuldades = False
    play = False
    Rank = False
    C = 0
    dificuldade = 1
    while True:
        constantes.cenario.draw()

        #Quando estiver na tela inicial do menu:
        if menu == True:
            constantes.botaoplay.draw()
            constantes.botaodif.draw()
            constantes.botaorank.draw()
            constantes.botaoexit.draw()
            if mouse.is_over_object(botaoexit) and mouse.is_button_pressed(1):
                janela.close()
            if mouse.is_over_object(botaoplay) and mouse.is_button_pressed(1):
                play = True
                menu = False
            if mouse.is_over_object(botaodif) and mouse.is_button_pressed(1):
                menu = False
                dificuldades = True
            if mouse.is_over_object(botaorank) and mouse.is_button_pressed(1):
                menu = False
                Rank = True

        #Quando estiver na tela de dificuldades:
        if dificuldades == True:
            constantes.botaofacil.draw()
            constantes.botaomedio.draw()
            constantes.botaodificil.draw()
            constantes.botaoback.draw()
            if mouse.is_over_object(botaofacil) and mouse.is_button_pressed(1):
                dificuldade = 1
                menu = True
                dificuldades = False
            if mouse.is_over_object(botaomedio) and mouse.is_button_pressed(1):
                dificuldade = 2
                menu = True
                dificuldades = False
            if mouse.is_over_object(botaodificil) and mouse.is_button_pressed(1):
                dificuldade = 3
                menu = True
                dificuldades = False
            if mouse.is_over_object(botaoback) and mouse.is_button_pressed(1) or teclado.key_pressed("ESC"):
                dificuldades = False
                menu = True

        #Quando estiver no gameloop vazio:
        if Rank == True:
            rank.exibir_ranking(janela)
        if teclado.key_pressed("ESC"):
            menu = True
            Rank = False

        if play == True:
            jogo.tela_do_jogo(mouse,teclado,dificuldade)


        janela.update()