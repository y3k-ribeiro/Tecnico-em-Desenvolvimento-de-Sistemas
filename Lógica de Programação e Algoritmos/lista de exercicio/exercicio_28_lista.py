matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para [{i},{j}]: "))
        linha.append(valor)
    matriz.append(linha)

soma_secundaria = 0
for i in range(3):
    soma_secundaria += matriz[i][2 - i]

print(f"Soma da diagonal secundária: {soma_secundaria}")