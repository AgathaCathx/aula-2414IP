#calcular o IMC
peso = float(input("qual seu peso?"))
altura = float(input("qual sua altura"))
IMC = peso /(altura * altura)
print(IMC)

if IMC >= 0 and IMC <= 18.4:
    print("voce tem um peso normal")
    pass

elif IMC >= 18.5 and IMC <= 24.9:
    print("voce tem sobre peso")
    pass

elif IMC >= 25 and IMC <= 30:
    print("sobrepeso")
    pass

elif IMC >= 31 and IMC <= 35:
    print("voce tem obesidade classe 1")
    pass

elif IMC >= 36 and IMC <= 40:
    print("voce tem obesidade classe 2")
    pass

elif IMC >= 41 and IMC <= 45:
    print("voce tem obesidade classe 3")
    pass

else:
    print("voce nao tem jeito mesmo! Vai se exercitar")