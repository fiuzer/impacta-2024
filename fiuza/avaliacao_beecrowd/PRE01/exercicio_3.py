preco = float(input())
quantidade = int(input())

valor_sem_desconto = preco * quantidade

desconto_fixo = 0.1
desconto_por_unidade = quantidade * 0.01
desconto_total = desconto_fixo + desconto_por_unidade

valor_com_desconto = valor_sem_desconto * (1 - desconto_total)

print(f'{valor_sem_desconto:.2f}')
print(f'{valor_com_desconto:.2f}')
