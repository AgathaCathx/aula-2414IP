nota1= float(input("Nota que voce tirou: "))
nota2= float(input("Segunda nota: "))
media = (nota1+nota2)/2
if media >=7 and media<=10:
    print(f'Sua media e de: {media}. VOCE PASSOU DE ANO!!!!!!!!!!!!!!!!!!!! SUA MAE NAO VAI TE ESPANCAR UUUUUHHHUUUULLLLL. ')
    pass
elif media <0 or media>10:
    print(f"media invalida")
    pass
else:
    print(f'Sua media e de: {media}. Voce nao passou, sua mae vai te espancar. Foi bom conhecer voce :(')