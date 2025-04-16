# Lê os três lados do triângulo
a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

# Verifica se os lados podem formar um triângulo
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os lados formam um triângulo!")

    # Identifica o tipo de triângulo
    if a == b and b == c:
        print("Tipo: TRIÂNGULO EQUILÁTERO")
    elif a == b or a == c or b == c:
        print("Tipo: TRIÂNGULO ISÓSCELES")
    else:
        print("Tipo: TRIÂNGULO ESCALENO")
else:
    print("Os lados NÃO formam um triângulo.")