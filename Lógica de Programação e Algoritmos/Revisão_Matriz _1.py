# Revisão Matriz 1
# Solicitar a quantidade de linhas
# Solicitar a quantidade de colunas
# Preencher a matriz
# Calcular a soma de todos os números
#----------------------------------------

# Passo 1) Variáveis
linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))
matriz = []
soma = 0

# Passo 2) Preencher matriz
# Sempre repetir quando preencher matriz
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input("Digite um número: ")))
    matriz.append(linha)

# Passo 3) Percorrer a matriz e calcular a soma
# Sempre repetir quando for percorrer a matriz
for i in range(linhas):
    for j in range(colunas):
        soma = soma + matriz[i][j]
print("A soma é: ", soma)