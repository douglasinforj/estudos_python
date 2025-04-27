"""
Solicite ao usuário que digite números inteiro positivos. Quando o usuário digitar um número negativo,
pare o programa e mostre a soma de todos os números digitados
"""

soma = 0
while True:
    num = int(input("Digite um número positivo (ou negativo para sair): "))
    if num < 0:
        break
    soma += num
print("Soma dos números digitados:", soma)