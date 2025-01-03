import os
from PPlay.window import *

# Nome do arquivo de ranking
RANKING_FILE = "ranking.txt"

def adicionar_pontuacao(nome, pontuacao):
    """
    Adiciona uma pontuação ao arquivo de ranking.
    :param nome: Nome do jogador
    :param pontuacao: Pontuação do jogador
    """
    # Abre o arquivo no modo append e adiciona a nova pontuação
    with open(RANKING_FILE, "a") as file:
        file.write(f"{nome}: {pontuacao}\n")

def ler_ranking():
    """
    Lê e retorna o ranking em ordem decrescente de pontuação.
    :return: Lista de tuplas (nome, pontuação)
    """
    if not os.path.exists(RANKING_FILE):
        return []
    
    with open(RANKING_FILE, "r") as file:
        linhas = file.readlines()
    
    ranking = []
    for linha in linhas:
        try:
            nome, pontuacao = linha.strip().split(":")
            ranking.append((nome, int(pontuacao)))
        except ValueError:
            pass  # Ignorar linhas mal formatadas
    
    # Ordena por pontuação em ordem decrescente
    ranking.sort(key=lambda x: x[1], reverse=True)
    vetor1 = []
    if(len(ranking) < 5):
        for i in range(len(ranking)):
            vetor1.append(ranking[i])
    else:
        for i in range(5):
            vetor1.append(ranking[i])
    return vetor1

def exibir_ranking(janela):
    """
    Exibe o ranking no console.
    """
    ranking = ler_ranking()
    janela.draw_text("===== Ranking =====",janela.width/2 - 100,((janela.height/4)-20),size=20,color=(255,255,255),font_name="Arial", bold=False, italic=False)
    for i, (nome, pontuacao) in enumerate(ranking, start=1):
        janela.draw_text(str(f"{i}. {nome} - {pontuacao}"), janela.width/2 - 100, ((janela.height/4)-20) + 50*i, size=20, color=(255,255,255),font_name="Arial", bold=False, italic=False)
    if not ranking:
       janela.draw_text("Nenhum registro no ranking ainda!",janela.width/2 - 100,((janela.height/4)-20),size=20,color=(255,255,255),font_name="Arial", bold=False, italic=False)
