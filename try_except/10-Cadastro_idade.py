"""
Peça idades até o usuário digitar "Sair". Trate entradas inválidas
"""

idades = []

while True:
    entrada = input("Digite uma idade ou 'sair' para encerrar.")
    if entrada.lower() == "sair":
        print('Voce saiu do programa.')
        break
    try:
        idade = int(entrada)
        idades.append(idade)
    except ValueError:
        print("Erro: Idade inválida. Tente novamente.")

    print(f"Idades Cadastradas: {idades}")






"""
Em Python, lower() é um método de string que converte todos os caracteres de uma string para minúsculas. 
Ele retorna uma nova string com todas as letras maiúsculas convertidas para minúsculas, 
enquanto outros caracteres (números, símbolos) permanecem inalterados. 
"""