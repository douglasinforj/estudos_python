"""
O programa escolhe um número entre 1 a 100. O usuário deve tentar adivinhar qual é. O programa deve dizer o palpite é muito alto 
ou muito baixo até acertar.

"""

import random

segredo = random.randint(1, 100)
tentativa = 0
palpite = 0

while palpite != segredo:
    palpite = int(input("Adivinhe o número entre 1 e 100: "))
    tentativa += 1
    if palpite < segredo:
        print("Muito Baixo!")
    elif palpite > segredo:
        print("Muito Alto!")
    else:
        print(f"Parabens! Voce Acertou em {tentativa} tentativas.")
