from game_rules import criarTabuleiro, verificarGanhador, imprimirTabuleiro, obterCoordenada, verificarCoordenadas, realizarJogada
from minimax import  jogadaIA

jogador1 = input("\nPlayer 1\n")
jogador2 = input("\nPlayer 2\n")
jogadores = [jogador2, jogador1]

tabuleiro = criarTabuleiro()
winner = False
jogador = 0


while(not winner):
    imprimirTabuleiro(tabuleiro)
    print(jogador)
    if(jogador == 0):
        linha, coluna = jogadaIA(tabuleiro, jogador)
    else:
        linha = obterCoordenada("linha")
        coluna = obterCoordenada("coluna")

    if(verificarCoordenadas(tabuleiro, linha, coluna)):
        realizarJogada(tabuleiro, linha, coluna, jogador)
        jogador = (jogador + 1) % 2

    winner = verificarGanhador(tabuleiro)

imprimirTabuleiro(tabuleiro)
if(winner != "Empate"):
    print("Jogador "+jogadores[jogador]+" venceu")
else:
    print(winner)
