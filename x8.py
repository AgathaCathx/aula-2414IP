#faca, um programa que peca a idade e verifique com a idade 
#se ele e crinca,adolescente, jovem, adulto ou idoso.
idade = int(input ("qual sua idade"))

if idade <=18:
    print("Você é menor de idade.")
    pass
elif idade >=21:
    print("Você é maior de idade, mas ainda é jovem!")
    pass

if idade >=25:
    print("Você é um adulto.")
    pass
else:
    print("Você é um adulto.")


if idade >=30:
    print("Você é um adulto")
    pass
else:
    print("Você é maior de idade")


if idade < 18:
    print("Você é crianca.")
    pass
else:
    print("Você é menor de idade.")

if idade > 18:
    print("Você é um idoso.")
    pass
else:
    print("Você é maior de idade.")



