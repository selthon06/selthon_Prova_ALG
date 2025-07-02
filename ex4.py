# Estrutura exemplo com 3 níveis de hierarquia
empresa = {
    'nome': 'João',
    'cargo': 'CEO',
    'salario': 10000.0,
    'subordinados': [
        {
            'nome': 'Maria',
            'cargo': 'Gerente',
            'salario': 7000.0,
            'subordinados': [
                {
                    'nome': 'Carlos',
                    'cargo': 'Analista',
                    'salario': 4000.0,
                    'subordinados': []
                }
            ]
        },
        {
            'nome': 'Ana',
            'cargo': 'Coordenadora',
            'salario': 6000.0,
            'subordinados': []
        }
    ]
}

# 1. Número total de funcionários
def contar_funcionarios(funcionario):
    total = 1  # conta o próprio funcionário
    for sub in funcionario['subordinados']:
        total += contar_funcionarios(sub)
    return total

# 2. Soma total da folha salarial
def somar_salarios(funcionario):
    total = funcionario['salario']
    for sub in funcionario['subordinados']:
        total += somar_salarios(sub)
    return total

# 3. Profundidade máxima da hierarquia
def profundidade_maxima(funcionario):
    if not funcionario['subordinados']:
        return 1
    profundidades = [profundidade_maxima(sub) for sub in funcionario['subordinados']]
    return 1 + max(profundidades)

# Testes com a estrutura exemplo
print("Total de funcionários:", contar_funcionarios(empresa))
print("Folha salarial total: R$", somar_salarios(empresa))
print("Profundidade máxima da hierarquia:", profundidade_maxima(empresa))