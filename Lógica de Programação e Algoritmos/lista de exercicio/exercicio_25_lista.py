linhas = 2
colunas = 3
matriz = []

print(f"Digite os elementos da matriz {linhas}x{colunas}:")


for i in range(linhas):
    linha = []
    for j in range(colunas):
        elemento = int(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

print("\n Matriz lida:")
for linha in matriz:
    print(linha)

print("\n Soma de cada coluna:")
for j in range(colunas):
    soma_coluna = 0
    for i in range(linhas):
        soma_coluna += matriz[i][j]
    print(f"Coluna {j+1}: {soma_coluna}")