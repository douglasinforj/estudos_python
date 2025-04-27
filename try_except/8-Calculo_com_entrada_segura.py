"""
Peça dois números em uma operação(+,-,*,/). Execute a operação. Trate todos os erros possíveis.
"""

class OperacaoInvalida(Exception):      #Criando uma Exceção Personalizada, Em Python, a gente cria uma exceção própria assim.
    pass                                #Isso cria um novo tipo de erro, igual os nativos (ValueError, ZeroDivisionError), mas com o nome que a gente quiser!

try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    op = input("Digite a operação (+, -, *, /): ")

    if op == "+":
        print(f"Resuldato: {a + b} ")
    elif op == "-":
        print(f"Resuldato: {a - b} ")
    elif op == "*":
        print(f"Resuldato: {a * b} ")
    elif op == "/":
        print(f"Resuldato: {a / b} ")
    else:
        raise OperacaoInvalida(f"Operação '{op}' não é suportada ")
    
except OperacaoInvalida as e:
    print(f"Erro de operação: {e}")
except ValueError:
    print("Erro: Entrada inválida. Digite apenas números")
except ZeroDivisionError:
    print("Erro: Divisão por zero")


"""
Em Python, "raise" é uma palavra-chave usada para lançar (gerar) uma exceção. 
Isso permite que você interrompa o fluxo normal do programa e sinalize 
que ocorreu um erro ou uma situação excepcional. Essa instrução é útil para 
tratar erros de forma programática e garantir que o código lide corretamente 
com condições inesperadas. 
"""   


