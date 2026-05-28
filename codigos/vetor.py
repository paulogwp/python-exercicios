
# Vetor não possui tamanho fixo o usuario pode definir

tamanho = int(input("Digite a quantidade de alunos: "))
vetor = []

for i in range(tamanho):
    valor = int(input(f"Digite a nota do aluno {i+1}: "))
    vetor.append(valor)

print("Notas dos alunos:", vetor)