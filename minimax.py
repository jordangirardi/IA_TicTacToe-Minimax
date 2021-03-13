from game_rules import simbolo, verificarGanhador

pontos = {
    "Empate": 0,
    "X": 1,
    "O": -1
}


def jogadaIA(tabuleiro, jogador):
    possibilidades = obterPosicoes(tabuleiro)
    melhorValor = None
    melhorJogada = None

    for possibilidade in possibilidades:
        tabuleiro[possibilidade[0]][possibilidade[1]] = simbolo[jogador]
        valor = miniMax(tabuleiro, jogador)
        tabuleiro[possibilidade[0]][possibilidade[1]]= " "

        if(melhorValor is None):
            melhorValor = valor
            melhorJogada = possibilidade
        elif(jogador == 0):
            if(valor > melhorValor):
                melhorValor = valor 
                melhorJogada = possibilidade
        elif(jogador == 1):
            if(valor < melhorValor):
                melhorValor = valor  
                melhorJogada = possibilidade

    return melhorJogada[0], melhorJogada[1]


def obterPosicoes(tabuleiro):
    posicoes = []

    for i in range(3):
        for j in range(3):
            if(tabuleiro[i][j] == " "):
                posicoes.append([i, j])

    return posicoes


def miniMax(tabuleiro, jogador):
    ganhador = verificarGanhador(tabuleiro)

    if(ganhador):
        return pontos[ganhador]

    jogador = (jogador+1) % 2
    melhorValor = None
    possibilidades = obterPosicoes(tabuleiro)

    for possibilidade in possibilidades:
        tabuleiro[possibilidade[0]][possibilidade[1]] = simbolo[jogador]
        valor = miniMax(tabuleiro, jogador)
        tabuleiro[possibilidade[0]][possibilidade[1]] = " "

        if(melhorValor is None):
            melhorValor = valor
        elif(jogador == 0):
            if(valor > melhorValor):
                melhorValor = valor
        elif(jogador == 1):
            if(valor < melhorValor):
                melhorValor = valor

    return melhorValor
