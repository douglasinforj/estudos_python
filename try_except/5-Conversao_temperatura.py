"""
Peça uma temperatura em Celsius e converta para Fahrenheit. Trate o erro de entrada inválida.
"""

try:
    celsius = float(input("Digite a temperatura em celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"Temperatura em Fahrenheit: {fahrenheit}")
except ValueError:
    print("Erro: Digite uma temperatura válida.")