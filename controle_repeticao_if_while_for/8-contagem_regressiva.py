"""
Escreva um programa que faça uma contagem regressiva de 10 até 0 e exiba "BOOM!" no final.
"""


for i in range(10, -1, -1):
    print(i)
print ("BooooMMM!!")



"""
-A linha for i in range(10, -1, -1): é uma instrução de repetição em Python que utiliza a função range() 
para gerar uma sequência de números. Vamos detalhar os três parâmetros dentro do range():

-Início (10): O primeiro número é o valor inicial da sequência. Nesse caso, começa de 10.

-Fim (-1): O segundo número é o valor onde a sequência irá parar, mas não inclui o número final. 
Como o valor final é -1, a sequência irá parar no 0, mas não vai incluir -1.

-Passo (-1): O terceiro número é o valor do "passo", ou seja, a quantidade de unidades que a 
sequência irá diminuir a cada iteração. Nesse caso, o passo é -1, o que significa que a sequência 
será gerada de forma decrescente.
"""