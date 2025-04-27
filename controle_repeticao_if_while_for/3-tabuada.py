"""
Peça ao usuário um número e imprima a tabuada desse número de 1 a 10
"""

num = int(input("Digite um número para ver sua tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")