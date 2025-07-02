alunos = {
    'Ana': [1, 1, 0, 1, 1],
    'Bruno': [1, 0, 0, 1, 0],
    'Clara': [1, 1, 1, 1, 1],
    'Daniel': [0, 0, 1, 1, 1]
}

aprovados = []

for nome, presencas in alunos.items():
    taxa_presenca = sum(presencas) / len(presencas)
    if taxa_presenca >= 0.7:
        aprovados.append(nome)

print("Alunos aprovados:", aprovados)