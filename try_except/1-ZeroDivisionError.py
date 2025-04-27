"""
Peça dois números ao usuário e divida o primeiro pelo segundo. Trate o erro de divisão por zero.
"""

try:
    a = float(input("Digite o numerador: "))
    b = float(input("Digite o denominador: "))
    resultado = a / b
    print(f"Resultado: {resultado}")

except ZeroDivisionError:
    print("Erro: Não é possivel dividir por zero.")
except ValueError:
    print("Você deve digitar numeros válido")

    