# importar as bibliotecas
import pandas as pd
import os 

dados = {
    "id": [],
    "Descrição": [],
    "Status": []
}
deseja_continuar = ""

while(deseja_continuar != "n"):
    print("\n Digite os dados: ")
    id = input("id: ")
    descricao = input("Descrição: ")
    status = int(input("Status: "))

    dados["id"].append(id)
    dados["Descrição"].append(descricao)
    dados["Status"].append(status)

    deseja_continuar = input("Deseja continuar? (s/n)").strip().lower()
    #strip() -> tirar espaços em branco
    #lower() -> transformar em minúsculo

df = pd.DataFrame(dados)
print(df)

#definir o  caminho onde será salvo o arquivo
os.chdir(" C:\\Users\\58956305889\\Documents\\leitura_manipulacao_ex03\\")
df.to_json("tarefas.json", sep="\t", index=False)
print("Dados salvos em 'tarefas.json'!")


#Leitura dos arquivos
try:
    df_lido = pd.read_csv("tarefas,json")
    print("\n Dados Carregados: ")
    print(df_lido)
except FileNotFoundError:
    print("\n Arquivo não encontrado!")