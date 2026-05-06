matriz = []
soma = 0

for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Digite o elemento [{i}][{j}]: "))
        linha.append(valor)
        soma += valor 
    matriz.append(linha)

print("\n Matriz 2x2:")
for linha in matriz:
    print(linha)

print(f"\n A soma de todos os elementos é: {soma}")