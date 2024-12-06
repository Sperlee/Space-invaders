import constantes
import jogo
from constantes import*
import resetar

#Função Menu:
def Menu (janela,mouse,teclado):
    #Variáveis condicionais:
    menu = True
    dificuldades = False
    play = False

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

        #Quando estiver na tela de dificuldades:
        if dificuldades == True:
            constantes.botaofacil.draw()
            constantes.botaomedio.draw()
            constantes.botaodificil.draw()
            constantes.botaoback.draw()
            if mouse.is_over_object(botaofacil) and mouse.is_button_pressed(1):
                constantes.dificuldade = 1
            if mouse.is_over_object(botaomedio) and mouse.is_button_pressed(1):
                constantes.dificuldade = 2
            if mouse.is_over_object(botaodificil) and mouse.is_button_pressed(1):
                constantes.dificuldade = 3
            if mouse.is_over_object(botaoback) and mouse.is_button_pressed(1):
                dificuldades = False
                menu = True

        #Quando estiver no gameloop vazio:
        if play == True:
            jogo.tela_do_jogo(mouse,teclado)


        janela.update()