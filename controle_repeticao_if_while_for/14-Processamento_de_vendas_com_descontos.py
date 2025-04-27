"""
Crie um sistema de vendas em que o usuário informa o valor da compra e, dependendo do valor da compra, um desconto é aplicado.
Se a compra for de R$ 500, um desconto de 10% é aplicado se for acima de R$300, o desconto é de 5%; caso contrário, não há desconto.
"""

valor_compra = float(input("Digite o valor total da compra: R$ "))

if valor_compra > 500:
    desconto = valor_compra * 0.10
elif valor_compra > 300:
    desconto = valor_compra * 0.05
else:
    desconto = 0

valor_final = valor_compra - desconto

print(f"Valor original: R${valor_compra:.2f}")
print(f"Desconto aplicado: R${desconto:.2f}")
print(f"Valor final com desconto: R${valor_final:.2f}")

"""
Conceitos aplicados:

Condicionais if, elif, e else

Cálculos e manipulação de valores financeiros

Condições de negócio para descontos
"""