positivos = 0
negativos = 0

for i in range(10):
    numero = float(input("Digite um número:"))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("Quantidade de positivos:", positivos )
print("Quantidade de negativos: ", negativos)