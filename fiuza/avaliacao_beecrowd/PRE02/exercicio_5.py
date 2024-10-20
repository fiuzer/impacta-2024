def calcular_notas_finais():
    # Pega o numero das notas dos alunos
    N = int(input().strip())
    
    # Le as primeias notas(originais)
    notas_originais = []
    for _ in range(N):
        nota = float(input().strip())
        notas_originais.append(nota)
    
    # Le as notas da segunda chance
    notas_segunda_chance = []
    for _ in range(N):
        nota = float(input().strip())
        notas_segunda_chance.append(nota)
    
    # Calcula as notas finais com o bonus
    notas_finais = []
    notas_alteradas = 0
    
    for i in range(N):
        nota_original = notas_originais[i]
        nota_segunda_chance = notas_segunda_chance[i]
        nota_final = nota_original
        
        if nota_segunda_chance == 10:
            nota_final += 2
            if nota_final > 10:
                nota_final = 10
        
        if nota_final != nota_original:
            notas_alteradas += 1
        
        notas_finais.append(nota_final)
    
    # Printa os resultados
    print(f"NOTAS ALTERADAS: {notas_alteradas}")
    
    for i in range(N):
        nota_original = notas_originais[i]
        nota_final = notas_finais[i]
        prefix = "*" if nota_final != nota_original else "-"
        print(f"{prefix}({i+1:03d}) original: {nota_original:05.2f} | final: {nota_final:05.2f}")

# Chama a função principal
calcular_notas_finais()
