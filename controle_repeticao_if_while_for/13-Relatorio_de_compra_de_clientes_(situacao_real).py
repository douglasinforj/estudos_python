"""
Voce tem uma sistema de compras e precisa gerar um relatorio das compras realizadas por um cliente.
O programa deve registrar os itens comprados e seus respectivos preços. Ao final, ele deve mostrar o total 
gasto pelo cliente e o item mais caro
"""

compras = []
total = 0

for i in range(3):   #registrar 3 vendas
    item = input("Digite o nome do item comprado: ")
    preco = float(input(f"Digite o preço de {item}: R$ "))
    compras.append((item, preco))   #adiciona tupla em uma lista (compras)
    total += preco

mais_caro = max(compras, key=lambda x: x[1])  
# função lambda recebe x(cada tupla) e retorna o segundo elemento da tupla no caso (preço)
# max() é uma funcao que encontra o maior elemento de uma coleção

print(f"Relatório de Compras:")
for item, preco in compras:
    print(f"{item}: R${preco:.2f}")

print(f"Total gasto: R${total:.2f}")
print(f"O item mais caro foi {mais_caro[0]} no valor de R${mais_caro[1]:.2f}")
#a variavel "mais_caro" recebeu os elementos da tupla, para acessar os elemento fazemos [0], e [1]


"""
Conceitos aplicados:

Armazenamento e manipulação de dados com tuplas e listas

Funções integradas como max()

Cálculo de totais e comparações
"""