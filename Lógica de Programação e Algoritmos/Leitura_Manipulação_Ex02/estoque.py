# importar as bibliotecas
import pandas as pd
import os 

dados = {
    "id": [],
    "Nome": [],
    "Quatidade": [],
    "Preço": []
}
deseja_continuar = ""

while(deseja_continuar != "n"):
    print("\n Digite os dados: ")
    id = input("id: ")
    nome = input("Nome: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))

    dados["id"].append(id)
    dados["Nome"].append(nome)
    dados["Quantidade"].append(quantidade)

    deseja_continuar = input("Deseja continuar? (s/n)").strip().lower()
    #strip() -> tirar espaços em branco
    #lower() -> transformar em minúsculo

df = pd.DataFrame(dados)
print(df)

#definir o  caminho onde será salvo o arquivo
os.chdir(" C:\\Users\\58956305889\\Documents\\Leitura_Manipulação_Ex02\\")
df.to_csv("dados.txt", sep="\t", index=False)
print("Dados salvos em 'estoque.csv'!")


#Leitura dos arquivos
try:
    df_lido = pd.read_csv("dados.csv")
    print("\n Dados Carregados: ")
    print(df_lido)
except FileNotFoundError:
    print("\n Arquivo não encontrado!")