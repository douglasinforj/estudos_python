"""
Você tem um sistema de vendas em que o usuário deve registrar as vendas realizadas em 
diferentes categorias(Eletrônicos, Roupas. Alimentos).
O Programa deve registrar a vendas de cada categoria e no final mostrar o total de vendas por categoria
"""

vendas_eletronicos = 0
vendas_roupas = 0
vendas_alimentos = 0

for i in range(5):    #registro de 5 vendas
    categoria = input("Digite a categoria da venda (Eletronicos, Roupas, Alimentos): ").lower()
    valor = float(input("Digite o valor da venda: R$"))

    if categoria == "eletronicos":
        vendas_eletronicos += valor
    elif categoria == "roupas":
        vendas_roupas += valor
    elif categoria == "alimentos":
        vendas_alimentos += valor
    else:
        print("Categoria inválida!")
    
print(f"Total em Eletrônicos: R${vendas_eletronicos:.2f}")
print(f"Total em Roupas: R$ {vendas_roupas:.2f}")
print(f"Total em Alimentos: R$ {vendas_alimentos:.2f}")