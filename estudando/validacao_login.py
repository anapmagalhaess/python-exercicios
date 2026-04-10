'''1. O Validador de Login (If/Else + Operadores Lógicos)
Objetivo: Criar um sistema que verifique nome de usuário e senha.

Crie uma variável usuario_salvo = "admin" e senha_salva = "123".

Peça para o usuário digitar um nome e uma senha.

Regra: Se o nome E a senha estiverem corretos, imprima "Acesso concedido". Caso contrário, imprima "Login ou senha incorretos".1. O Validador de Login (If/Else + Operadores Lógicos)
Objetivo: Criar um sistema que verifique nome de usuário e senha.

Crie uma variável usuario_salvo = "admin" e senha_salva = "123".

Peça para o usuário digitar um nome e uma senha.

Regra: Se o nome E a senha estiverem corretos, imprima "Acesso concedido". Caso contrário, imprima "Login ou senha incorretos".'''

usuario_salvo = "admin"
senha_salva = 123

usuario_inserido = str(input("Insira o usuário: "))
senha_inserida = int(input("Insira a senha: "))

if usuario_inserido == usuario_salvo and senha_inserida == senha_salva:
    print("Acesso Concedido.")
else:
    print ("Login ou senha incorretos.")