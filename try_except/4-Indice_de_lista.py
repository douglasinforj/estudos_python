"""
Acesse um índice informado pelo usuário de uma lista. Trate o erro caso o índice seja inválido.
"""

lista = [10, 20, 30, 40, 50]

try:
    indice = int(input("Digite o indice que deseja acessar (0 a 4)"))
    print(f"Valor: {lista[indice]}")
except IndexError:
    print("Erro: Índice fora do intervalo.")
except ValueError:
    print("Erro: Indice Invalido, digite um número")