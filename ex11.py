preço = float(input("digite o preço do produto:"))
desconto = preço * 0.05
promoçao = preço - desconto
print(f"o preço promocional do produto com 5% de desconto e: RS {promoçao:.2f}")