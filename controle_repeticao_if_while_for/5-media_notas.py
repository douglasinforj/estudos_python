"""
Peça as notas de 5 alunos e calcule a média da turma
"""

soma = 0
for i in range(1, 6):
    nota = float(input("Digite a nota do aluno {i}: "))
    soma += nota

media = soma / 5
print(f"A média da turma é: {media:.2f}")