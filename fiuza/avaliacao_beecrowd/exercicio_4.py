n = int(input())

if n < 2:
  print("O número deve ser maior ou igual a 2.")
elif n % 2 == 0:
  impar_anterior = n - 1
else:
  impar_anterior = n - 2
if n % 2 == 0:
  par_posterior = n + 2
else:
  par_posterior = n + 1

print(f'{impar_anterior} {par_posterior}')
