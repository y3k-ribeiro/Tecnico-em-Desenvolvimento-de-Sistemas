idade = int(input("Digite sua idade: "))

if(idade >= 0 and idade <= 12 ):
    print("Criança")
if(idade >= 13 and idade >=17):
    print("Adolescente")
elif(idade >= 18 and idade >= 59):
    print("Adulto")
elif(idade>=60):
    print("Idoso")
else:
    print("Idade Incorreta")
    


    