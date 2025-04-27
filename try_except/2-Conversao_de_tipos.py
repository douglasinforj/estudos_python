"""
Peça um número inteiro ao usuário e converta para inteiro(int). Trate caso o valor digitado não seja valido.
"""

try:
    numero = int(input("Digite um número inteiro"))
    print(f"Número digitado: {numero}")
except:
    print("Erro: Isso não é um numero inteiro")