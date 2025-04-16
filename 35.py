def calcular_valor_final(tipo_carro, dias, km_percorridos):
    # Definindo os valores fixos
    if tipo_carro == 'popular':
        aluguel_diario = 90  # valor diário para carro popular
        if km_percorridos <= 100:
            valor_km = 0.20  # valor por Km se até 100 Km
        else:
            valor_km = 0.10  # valor por Km se mais de 100 Km
    elif tipo_carro == 'luxo':
        aluguel_diario = 150  # valor diário para carro de luxo
        if km_percorridos <= 200:
            valor_km = 0.30  # valor por Km se até 200 Km
        else:
            valor_km = 0.25  # valor por Km se mais de 200 Km
    else:
        print("Tipo de carro inválido.")
        return
    
    valor_aluguel = dias * aluguel_diario
    valor_km_total = km_percorridos * valor_km
    valor_total = valor_aluguel + valor_km_total
    
    return valor_total

tipo_carro = input("Digite o tipo de carro (popular ou luxo): ").strip().lower()
dias = int(input("Quantos dias de aluguel? "))
km_percorridos = float(input("Quantos Km foram percorridos? "))

valor_total = calcular_valor_final(tipo_carro, dias, km_percorridos)

if valor_total is not None:
    print(f"O valor total a ser pago é: R${valor_total:.2f}")