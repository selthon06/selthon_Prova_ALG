import random

def aplicar_desconto(valor):
    sorteio = random.randint(1, 100)
    if sorteio <= 30:
        desconto = 0.10
    elif sorteio <= 70:
        desconto = 0.25
    else:
        desconto = 0.50
    valor_final = valor * (1 - desconto)
    return f'{valor_final:,.2f}'.replace('.', ',')  # formata com vírgula

# Exemplo:
valor_original = 100.0
print("Valor com desconto aplicado:", aplicar_desconto(valor_original))