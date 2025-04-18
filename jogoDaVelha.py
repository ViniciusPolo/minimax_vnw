import math
import random

# Tabuleiro representado como lista de 9 elementos
tabuleiro = [" " for _ in range(9)]

def mostrar_tabuleiro():
    print("-" * 13)
    for i in range(3):
        linha = [tabuleiro[i * 3 + j] for j in range(3)]
        print("| " + " | ".join(linha) + " |")
        if i < 2:
            print("|---|---|---|")
    print("-" * 13)

def verificar_vencedor(b):
    posicoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
        [0, 4, 8], [2, 4, 6]              # diagonais
    ]
    for posicao in posicoes:
        if b[posicao[0]] == b[posicao[1]] == b[posicao[2]] != " ":
            return b[posicao[0]]
    if " " not in b:
        return "Empate"
    return None

def minimax(b, melhor_jogada, profundidade):
    resultado = verificar_vencedor(b)
    if resultado == "X":
        return 1
    elif resultado == "O":
        return -1
    elif resultado == "Empate" or profundidade == 0:
        return 0

    print(f"Possibilidades testadas: ${profundidade}") # Print interessante, mostra a IA pensando
    if melhor_jogada:
        melhor_pontuacao = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                pontuacao = minimax(b, False, profundidade - 1)
                b[i] = " "
                melhor_pontuacao = max(melhor_pontuacao, pontuacao)
        return melhor_pontuacao
    else:
        melhor_pontuacao = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                pontuacao = minimax(b, True, profundidade - 1)
                b[i] = " "
                melhor_pontuacao = min(melhor_pontuacao, pontuacao)
        return melhor_pontuacao
def melhor_jogada(profundidade):
    melhor_pontuacao = -math.inf
    movimento = None
    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro[i] = "X"
            pontuacao = minimax(tabuleiro, False, profundidade - 1) 
            tabuleiro[i] = " "
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                movimento = i
    return movimento

# Loop do jogo
print("Você é 'O'. IA é 'X'.")
dificuldade = (math.trunc(int(input("Digite 90%, 80%, ..., 10% para dificuldade (quanto mais alto, mais difícil):\n")) / 10)) - 1
profundidade = int(input("Determine a profundidade (1 a 8):\n"))
profundidade = max(1, min(profundidade, 8))
dificuldade = max(0, dificuldade)

while True:
    mostrar_tabuleiro()

    # Jogador humano
    try:
        pos = int(input("Escolha sua posição (0-8): "))
        if pos < 0 or pos > 8 or tabuleiro[pos] != " ":
            print("Posição inválida ou ocupada. Tente de novo.")
            continue
        tabuleiro[pos] = "O"
    except ValueError:
        print("Entrada inválida. Digite um número entre 0 e 8.")
        continue

    if verificar_vencedor(tabuleiro):
        break

    # Jogada da IA
    sorteio = random.randint(0, dificuldade)
    if sorteio == 0:
        disponiveis = [i for i in range(9) if tabuleiro[i] == " "]
        jogada = random.choice(disponiveis)
        print("IA jogou aleatoriamente.")
    else:
        jogada = melhor_jogada(profundidade)
        print("IA usou minimax.")

    tabuleiro[jogada] = "X"

    if verificar_vencedor(tabuleiro):
        break

# Resultado final
mostrar_tabuleiro()
resultado = verificar_vencedor(tabuleiro)
if resultado == "Empate":
    print("Deu empate!")
else:
    print(f"{resultado} venceu!")
