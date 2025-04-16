numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))


if numero1 > numero2:
    print("O primeiro valor é o maior")
elif numero2 > numero1:
    print("O segundo valor é o maior")
else:
    print("Não existe valor maior, os dois são iguais")