inicio = int(input('Início: '))
fim = int(input('Fim: '))

while inicio <= fim:
    print(f'x:{inicio}')
    inicio += 1

while inicio >= fim:
        print(f'x:{inicio}')
        inicio -= 1 
        if (inicio < 0):
              break