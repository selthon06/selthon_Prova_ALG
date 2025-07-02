import random

setores = {
    'Administrativo': ['Ana', 'João', 'Marcos'],
    'Operacional': ['Carlos', 'Bruna', 'Rita'],
    'Técnico': ['Lucas', 'Fernanda', 'Pedro']
}

setor_sorteado = random.choice(list(setores.keys()))
funcionario_sorteado = random.choice(setores[setor_sorteado])

print(f'Setor sorteado: {setor_sorteado}')
print(f'Funcionário sorteado: {funcionario_sorteado}')