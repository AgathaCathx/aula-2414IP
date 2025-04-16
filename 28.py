largura = float(input("Digite a largura do terreno (em metros): "))
comprimento = float(input("Digite o comprimento do terreno (em metros): "))

area = largura * comprimento

print(f"A área do terreno é: {area} m²")

if area < 100:
    print("TERRENO POPULAR")
elif 100 <= area <= 500:
    print("TERRENO MASTER")
else:
    print("TERRENO VIP")