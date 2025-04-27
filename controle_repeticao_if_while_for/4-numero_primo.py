"""
Peça um número primo ao usuário e diga se ele é ou não um número primo
"""

num = int(input("Digite um número: "))
eh_primo = True

if num <=1:
    eh_primo = False

# Se o número não for menor ou igual a 1:
else:
    for i in range(2, num):     #Começa um laço for que vai testar todos os números de 2 até (num - 1).
        if num % i == 0:        #Se o resto for 0, significa que num é divisível por i (ou seja, num não é primo).
            eh_primo = False    #Define eh_primo = False.
            break               #Usa break para sair do laço imediatamente (não precisa testar mais nada)

if eh_primo:
    print("É primo!")
else:
    print("Não é primo.")


"""
Explicação do código


Se o número não for menor ou igual a 1:
   Começa um laço for que vai testar todos os números de 2 até (num - 1).
   num % i calcula o resto da divisão de num por i.
       Se o resto for 0, significa que num é divisível por i (ou seja, num não é primo).

Se isso acontecer, o programa:

Define eh_primo = False.

Usa break para sair do laço imediatamente (não precisa testar mais nada).


"""