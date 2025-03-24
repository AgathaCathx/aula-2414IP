percorridos = float(input("digite a quantiddade de km percorridos : "))
dias_al = int(input("digite a quantidade de dias alugados: "))
preço_dia = 90.00
preço_km = 0.20
total = (dias_al*preço_dia) + (percorridos*preço_km)
print (f"o preço total a pagar e: {total:.2f}")