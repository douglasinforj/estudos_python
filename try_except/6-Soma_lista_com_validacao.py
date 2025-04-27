"""
Peça ao usuário para digitar 5 números e some todos. Ignore valores inválidos com aviso.
"""

numeros = []
for i in range(5):
    try:
        num = float(input(f"Digite o número {i+1}: "))
        numeros.append(num)
    except ValueError:
        print("Valor inválido, será ignorado.")

print(f"Soma dos npumero válidos: {sum(numeros)} ")