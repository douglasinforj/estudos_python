"""
Leia 10 números do usuário e diga quantos são pares e quantos são ímpares.
"""

pares = 0
impares = 0

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Pares: {pares} | Ímpares: {impares}")
