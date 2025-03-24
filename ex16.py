cigarros_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("Digite o número de anos fumando: "))
minutos_cigarro = 10  
dias_ano = 365 
minutos_dia = cigarros_dia * minutos_cigarro
minutos_total = minutos_dia * anos_fumando * dias_ano
print(f'O fumante perderá aproximadamente {minutos_dia:.2f} dias de vida.')