nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário atual: R$ "))
anos = int(input("Digite o tempo de empresa (em anos): "))

# Calcula o aumento de acordo com o tempo de empresa
if anos < 3:
    aumento = salario * 0.03
elif 3 <= anos < 10:
    aumento = salario * 0.125
else:
    aumento = salario * 0.20

# Calcula o novo salário
novo_salario = salario + aumento

# Mostra os resultados
print("\n--- Resultado ---")
print(f"Funcionário: {nome}")
print(f"Salário antigo: R$ {salario:.2f}")
print(f"Aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")