# Pega o número natural
n = int(input())

# Cria a pirâmide de Letras(alfabética)
for i in range(1, n + 1):
  c = chr(64 + i)
  
  print(c * i)