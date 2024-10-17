n = int(input())
cont = 1

for _ in range(10):
  if 0 <= n <= 10:
    print(f'{n} x {cont} = {n * cont}')
  cont += 1