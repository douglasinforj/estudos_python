"""
Dado um dicionario de pessoas, peça um nome e retorne a idade. Trate caso o nome não exista.
"""

pessoas = {"Ana":25, "Bruno": 30, "Carlos": 22}

try:
    nome = input("Digite o nome da pessoa: ")
    print(f"Idade de {nome}: {pessoas[nome]}")
except KeyError:
    print("Erro: Pessoa não encontrada")