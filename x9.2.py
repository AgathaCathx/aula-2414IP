#faça um programa que peça a idade e verifique com a idade se ele e bebe, crinça, adolecente, adulto ou idoso

idade = int(input ("qual sua idade"))

if idade >= 0 and  idade <= 4:
    print("voce e um bebezinho")
    pass

elif idade >= 5 and idade <= 13:
    print("voce e uma crinca")
    pass

elif idade >= 13 and idade <= 21:
    print("voce e um adolescente")
    pass

elif idade >= 22 and idade <= 59:
    print("voce e adulto")
    pass

elif idade >= 60 and idade <= 200:
    print("voce e um idoso")
    pass

else:
    print("voce ja virou po ou degradou na natureza")
    pass