"""
Tente abrir um arquivo chamado dados.txt e exiba seu conteúdo. Trate o erro caso o arquivo não exista.
"""

try:
    with open("dados.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

except FileNotFoundError:
    print("Erro: O arquivo 'dados.txt' não foi encontrado.")