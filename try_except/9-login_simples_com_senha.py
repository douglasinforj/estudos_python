"""
Simule um sistema de login. Usuário tem 3 tentativas. Trate erros de digitação e número de tentativas.
"""

senha_correta = "1234"
tentativas = 0

while tentativas < 3:
    try:
        senha = input("Digite a senha: ")
        if senha == senha_correta:
            print("Acesso concedido.")
        else:
            raise ValueError("Senha incorreta")
    except ValueError as e:
        print(e)
        tentativas +=1

if tentativas == 3:
    print("Número de tentativas excedido. Acesso Bloqueado.")


"""
Em Python, "raise" é uma palavra-chave usada para lançar (gerar) uma exceção. 
Isso permite que você interrompa o fluxo normal do programa e sinalize 
que ocorreu um erro ou uma situação excepcional. Essa instrução é útil para 
tratar erros de forma programática e garantir que o código lide corretamente 
com condições inesperadas. 
""" 