def bissexto(ano):
    """Função para verificar se um ano é bissexto ou  não"""
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False

def anos_bissextos(inicio, fim):
    """Função que retorna uma lista de anos bissextos entre inicio e fim"""
    bissextos = []
    for ano in range(inicio, fim + 1):
        if bissexto(ano):
            bissextos.append(ano)
    return bissextos

# Leitura dos valores de entrada
inicio = int(input(""))
fim = int(input(""))

# Obtenção da lista de anos bissextos
bissextos = anos_bissextos(inicio, fim)

# Impressão dos anos bissextos
for ano in bissextos:
    print(ano)

# Impressão da quantidade de anos bissextos
print(f"bissextos: {len(bissextos)}")
