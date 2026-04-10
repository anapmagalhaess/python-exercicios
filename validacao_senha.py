"""Crie um programa que solicite ao usuário uma senha. Enquanto a senha digitada estiver incorreta, o programa deve continuar pedindo novamente. Quando o usuário acertar, exiba uma mensagem de acesso permitido.
Regras:
Defina uma senha fixa no código (por exemplo: 1234)
Utilize while para repetir até acertar
Exemplo:
Digite a senha: 1111
Senha incorreta!
Digite a senha: 1234
Acesso permitido!"""

senhaUsuario = int(input('Envie sua senha: '))

while True:
    senhaTentativa = int(input('Digite a senha inserida: '))
    if senhaTentativa != senhaUsuario:
        print('Senha incorreta. Tente novamente')
    else:
        print('Acesso permitido!')
        break