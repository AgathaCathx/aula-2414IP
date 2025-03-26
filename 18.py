ano_que_nasceu = int(input("Em que ano voce nasceu:" ))
idade = (2025 - ano_que_nasceu)
if idade  >= 18:
    print(f"Nossa! VOCE PODE VOTAR!!!!!!! VOTEM EM AGATHA!")
    pass
else:
    print(f'voce e muito novo. Nao pode votar!!! {idade} ')
 