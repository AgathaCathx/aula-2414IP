import random

# O computador sorteia um número entre 1 e 5
numero_sorteado = random.randint(1, 5)

# O jogador tenta adivinhar
tentativa = int(input("Tente adivinhar o número sorteado (entre 1 e 5): "))

# Verifica se o jogador acertou
if tentativa == numero_sorteado:
    print("Parabéns! Você acertou o número!")
else:
    print(f"Você errou! O número sorteado era {numero_sorteado}.")