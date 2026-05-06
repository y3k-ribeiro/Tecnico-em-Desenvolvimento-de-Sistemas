# importar as bibliotecas
import pandas as pd
import os 

dados = {
    "Nome": [],
    "Disciplina": [],
    "Nota": []
}
deseja_continuar = ""

while(deseja_continuar != "n"):
    print("\n Digite os dados: ")
    nome = input("Nome: ")
    disciplina = input("Disciplina: ")
    nota = input("Nota: ")

    dados["Nome"].append(nome)
    dados["Disciplina"].append(disciplina)
    dados["Nota"].append(nota)

    deseja_continuar = input("Deseja continuar? (s/n)").strip().lower()
    #strip() -> tirar espaços em branco
    #lower() -> transformar em minúsculo

df = pd.DataFrame(dados)
print(df)

print("\n Escolha o formato para salvar os dados: ")
print("1 - TXT")
escolha_arquivo = input("Digite o  número do formato desejado: ")

#definir o  caminho onde será salvo o arquivo
os.chdir("C:\\Users\\58956305889\\Documents\\Leitura_Manipulação_Ex01\\")


if(escolha_arquivo == "1"):
    df.to_csv("dados.txt", sep="\t", index=False)
    print("Dados salvos em 'dados.txt'!")
else:
    print("Escolha inválida! Os dados não foram salvos!")

#Leitura dos arquivos
try:
    df_lido = pd.read_csv("dados.txt", sep="\t")
    print(df_lido)
except FileNotFoundError:
    print("\n Arquivo não encontrado!")