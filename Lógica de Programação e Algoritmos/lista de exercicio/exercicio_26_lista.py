maior_numero = None

while True:
    try:
        numero = int(input("Digite um número (0 para sair): "))
        
        if numero == 0:
            break
        
        if maior_numero is None or numero > maior_numero:
            maior_numero = numero
            
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if maior_numero is not None:
    print(f"O maior número digitado foi: {maior_numero}")
else:
    print("Nenhum número foi digitado além do zero.")