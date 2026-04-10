'''Classificador de Nadador (If/Elif/Else)
Objetivo: Praticar condições encadeadas.

Receba a idade de um nadador e classifique-o:

Menor que 5 anos: "Não pode competir".

5 a 7 anos: "Infantil A".

8 a 10 anos: "Infantil B".

11 a 17 anos: "Juvenil".

18 anos ou mais: "Adulto".'''

idade_usuario = int(input("Insira sua idade: "))

if idade_usuario < 5:
    print("Não pode competir.")
elif idade_usuario < 8:
    print("Infantil A")
elif idade_usuario < 11:
    print("Infantil B")
elif idade_usuario < 18:
    print("Juvenil")
else:
    print("Adulto")