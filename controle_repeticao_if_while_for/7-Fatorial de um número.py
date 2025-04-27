"""
Fatorial
O fatorial (!) de um número n, representado por n!, 
é a multiplicação de n por seus antecessores maiores ou iguais a 1. 
Essa operação é muito comum em análise combinatória.
"""

"""
Peça ao usuário um número inteiro e calcule o seu fatorial.
"""

num = int(input("Digite um numero para calcular o fatorial: "))

fatorial = 1

for i in range(1, num + 1):
    fatorial *= i

print(f"O fatorial de  {num} é {fatorial:.2f}")