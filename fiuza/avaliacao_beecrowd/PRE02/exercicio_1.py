# Pega as notas
nota_trab = float(input())
nota_prova = float(input())
# Realiza a média
media = (nota_trab + nota_prova) / 2
nota_sub = 12 - nota_trab

# Checa e apresenta qual é a situação do aluno
if media >= 6:
  print("aprovado")
elif nota_sub <= 10:
  print("talvez com a sub")
else:
  print("reprovado")