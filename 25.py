reta1 = float(input("qual o tamanho da reta?:"))
reta2 = float(input("qual o tamanho dessa segunda reta?:"))
reta3 = float(input("qual o tamanho dessa terceira reta?:"))
conta = (reta1+reta2+reta3)
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f"as retas {reta1}, {reta2}, {reta3} podem formar um triangulo")
else:
     print(f"as retas {reta1}, {reta2}, {reta3} nao podem formar um triangulo")