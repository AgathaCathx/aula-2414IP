# Leitura da distância em metros
metros = float(input("Digite a distância em metros: "))

km = metros / 1000  # 1 km = 1000 metros
cm = metros * 100  # 1 metro = 100 centímetros
mm = metros * 1000  # 1 metro = 1000 milímetros

print(f"A distância de {metros} metros corresponde a:")
print(f"{km} quilômetros")
print(f"{cm} centímetros")
print(f"{mm} milímetros")