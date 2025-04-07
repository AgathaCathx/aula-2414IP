sexo = (input("qual seu sexo?:"))
nome = (input("qual seu nome?:"))
compra = float(input("qual o valor da compra?:"))
if sexo == "masculino":
    desconto_masculino = 0.05 * compra
    valor_compra = compra - desconto_masculino
    print(f"Sua compra com desconto de 5% ficou {valor_compra}")
    pass
elif sexo == "feminino":
    desconto_feminino = 0.13 * compra
    valor_compra = compra - desconto_feminino
    print(f"Sua compra com desconto de 13% ficou {valor_compra}")