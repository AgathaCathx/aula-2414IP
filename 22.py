#primeiro passo; pedir a data denascimento: 2 passo: diminuir o ano atual - o ano que nasceu; 3 passo: fazer o if; 4 passo: fazer a pergunta
data = int(input("qual o ano que voce nasceu?"))
idade = (2025 - (data))
if idade <=17:
    print("voce pode fugir do brasil e nao se alistar, depois vere um terrorista")
else:
    print("voce pode se alistar")