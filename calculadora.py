#contador = 0
#while contador < 5:
#    print(f"contagem: {contador}")
#    contador += 1 

#senha = "1234"
#tentativa = ""
#while tentativa != senha:
#    tentativa = input("digite a senha:")
#print("Acesso concedido!")

#while True:
#    comando= input("digite 'sair' para parar:")
#    if comando.lower() == "sair":
#        print("ate a proxima")
#        break
#    print(f"voce digitou: {comando}")

#calculadora simples usando while
while True:
    comando = input("Digite 'sair' para parar: ")
    operacao = input("escolha a operaçao: (+,-,*,/)")
    num1 = float(input("escreva um numero:"))
    num2 = float(input("digite o outro numero"))
    if comando.lower() == "sair":
          print("Goodbye!")
          break
    if operacao =='+':
         print(num1+num2)
         pass
    elif operacao == '-':
         print(num1-num2)
         pass
    elif operacao == '*':
         print(num1*num2)
         pass
    elif operacao == '/':
         print(num1/num2)
         pass
    else:
         print("se colocar diferente de {operacao}, sera invalido")
         pass