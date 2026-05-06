num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = 0
for i in range(num1,num2):
    if(i%2 == 0):
        soma = soma + i
print("A soma de todos os números é:", soma)


    
