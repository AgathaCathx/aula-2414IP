distancia = float(input("qual a distancia que voce deseja percorrer em KM?:"))
if distancia <= 200:
    preco = distancia * 0.50
    print(f"o perco da passagem sera {preco: .2f}")
    pass
else:
    preco = distancia  * 0.45
    print(f"o perco da passagem sera {preco: .2f}")