a = float(input("Digite o valor da primeira reta: "))
b = float(input("Digite o valor da segunda reta: "))
c = float(input("Digite o valor da terceira reta: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("As retas formam um triângulo. ")
else:
    print("As retas não formam um triângulo. ")
