"""
Voce foi contratado para calcular o slário liquido de um funcionário. O Salário é informado pelo usuário
e o programa deve descontar 10% de importo de renda e 5% de INSS. Imprima o slário líquido após descontos.
"""

salario_bruto = float(input("Digite o salário bruto: R$"))
desconto_ir = salario_bruto * 0.10
desconto_iss = salario_bruto * 0.05
salario_liquido = salario_bruto - desconto_ir - desconto_iss

print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto de IR: R$ {desconto_ir:.2f}")
print(f"Desconto de INSS: R$ {desconto_iss:.2f}")
print(f"Salário liquido: R$ {salario_liquido:.2f}")

"""
Conceitos aplicados:

Entrada de dados

Cálculos matemáticos

Formatação de saída

"""