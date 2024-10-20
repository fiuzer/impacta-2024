def soma(n):
  soma = 0
  while n > 0:
    digito = n % 10
    if digito % 2 != 0:
      soma += digito
    n //= 10
  return soma

n = int(input("Digite um número natural: "))
resultado = soma(n)
print(f'A soma dos digitos impares é: {resultado}')