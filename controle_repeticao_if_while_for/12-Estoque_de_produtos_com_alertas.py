"""
Você é responsavel pelo controle de estoque de uma loja. O programa deve permitir adicionar a quantidade de produtos no estoque
e, sempre que a quantidade de um produto atingir o limite de alert (quantidade < 5), o sistema deve emitir um alerta de reposição
"""

estoque = {
    "Produto A": 10,
    "Produto B": 3,
    "Produto C": 15,
}

limite_estoque = 5

for produto, quantidade in estoque.items():
    print(f"{produto}: {quantidade} unidades")
    if quantidade < limite_estoque:
        print(f"Alerta! O estoque de {produto} está abaixo do limite!")