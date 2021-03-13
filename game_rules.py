import os
def clear(): return os.system("clear")

simbolo = ["X", "O"]

def criarTabuleiro():
    return ([
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ])

def verificarGanhador(tabuleiro):
    # linhas
    for i in range(3):
        if(tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != " "):
            return tabuleiro[i][0]

    # coluas
    for i in range(3):
        if(tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != " "):
            return tabuleiro[0][i]

    # diagonal esquerda
    if(tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != " "):
        return tabuleiro[0][0]

    # diagonal direita
    if(tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]  and tabuleiro[0][2] != " "):
        return tabuleiro[0][2]

    
    for i in range(3):
        for j in range(3):
            if(tabuleiro[i][j] == " "):
                return False
    
    return "Empate"

def imprimirTabuleiro(tabuleiro):
    limparConsole()
    for i in range(3):
        print("|".join(tabuleiro[i]))


def obterCoordenada(tipoCoordenada):
    try:
        imprimirLinha()
        coordenada = int(input("Informe a " + tipoCoordenada+"\n"))

        if(coordenada > 3 or coordenada < 1):
            print("A coordenada precisa estar entre 1 e 3\n")
            return obterCoordenada(tipoCoordenada)
        else:
            return coordenada-1

    except ValueError:
        print("Por favor, digite um numero válido")
        return obterCoordenada(tipoCoordenada)


def realizarJogada(tabuleiro, linha, coluna, jogador):
    tabuleiro[linha][coluna] = simbolo[jogador]
    imprimirLinha()


def verificarCoordenadas(tabuleiro, linha, coluna):

    if (tabuleiro[linha][coluna] == " "):
        return True
    else:
        print("=============================================")
        print("\nPosicao ocupada, informe uma posicao livre\n")
        return False


def imprimirLinha():
    print("\n=============================================\n\n")

def limparConsole(): 
    clear()