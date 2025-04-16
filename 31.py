import random

# Opções do jogo
opcoes = ["pedra", "papel", "tesoura"]

# Entrada do jogador
jogador = input("Escolha: pedra, papel ou tesoura: ").lower()

# Verifica se a escolha do jogador é válida
if jogador not in opcoes:
    print("Escolha inválida!")
else:
    # Escolha do computador
    computador = random.choice(opcoes)

    # Mostra as escolhas
    print(f"\nVocê escolheu: {jogador}")
    print(f"O computador escolheu: {computador}")

    # Verifica o resultado
    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Você venceu!")
    else:
        print("Você perdeu!")