'''3. Calculadora de Menu (Match Case)
Objetivo: Usar a estrutura de seleção para um menu simples.

Peça dois números ao usuário.

Mostre um menu: 1 - Somar, 2 - Subtrair, 3 - Multiplicar.

Use o match case para realizar a operação escolhida e mostrar o resultado.

Use o case _ para tratar se o usuário digitar uma opção inválida.'''

n1 = int(input("Envie o primeiro número: "))
n2 = int(input("Envie o segundo número: "))

print("=" * 20)
menu = int(input("1- Somar \n2- Subtrair \n3- Multiplicar \nDigite: "))

match menu:
    case 1:
        print("-" * 5 , "Somar")
        resultado = n1 + n2
        print(f"Resultado {resultado}")
    case 2:
        print("-" * 5 , "Subtrair")
        resultado = n1 - n2
        print(f"Resultado {resultado}")
    case 3:
        print("-" * 5 , "Multiplicador")
        resultado = n1 * n2
        print(f"Resultado {resultado}")
    case _:
        print("Opção inválida.")

