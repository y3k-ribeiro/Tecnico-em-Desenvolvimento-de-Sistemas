vetor = []
soma = 0

for i in range(7):
    num = int(input("Digite um número: "))
    vetor.append(num)

for numero in vetor:
    print(numero)
    soma = soma + numero
print("A soma de todos os elementos do vetor é: ", soma)
