n1 = float(input("Digite a primeira nota: ").replace(",", "."))
n2 = float(input("Digite a segunda nota: ").replace(",", "."))
n3 = float(input("Digite a terceira nota: ").replace(",", "."))

media_ponderada = (n1 * 2 + n2 * 4 + n3 * 8) / (2 + 4 + 8)

print(f"A média das notas é: {media_ponderada:.2f}")
