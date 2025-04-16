# Lê os dados do comprador
valor_casa = float(input("Qual o valor da casa? R$ "))
salario = float(input("Qual o seu salário? R$ "))
anos = int(input("Em quantos anos você vai pagar? "))

# Calcula o valor da prestação mensal
prestacao = valor_casa / (anos * 12)

# Verifica se a prestação mensal é maior que 30% do salário
limite_prestacao = salario * 0.30

# Verifica se o empréstimo é aprovado
if prestacao > limite_prestacao:
    print("Empréstimo NEGADO! A prestação mensal excede 30% do seu salário.")
else:
    print(f"Empréstimo APROVADO! A prestação mensal será de R$ {prestacao:.2f}.")