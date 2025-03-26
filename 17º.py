velocidade = float(input("Digite sua velocidade: "))
if velocidade >= 80: 
    multa = (velocidade - 80) * 5
    print(f'sua velocidade foi maior que o exigido voce receberá {multa}. pela ultrapassagem')
    pass
else: 
    print(f'sua velocidade foi menor que {velocidade} voce nao recebera nenhuma multa')
