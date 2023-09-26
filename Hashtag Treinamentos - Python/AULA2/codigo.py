# Passo a Passo:
# Passo 1: Importar a base de dados
# Passo 2: Visualizar a base de dados
# Passo 3: Corrigir erros da base de dados
# Passo 4: Primeira análise do cancelamento dos clientes (Qual o % de clientes que cancelou)
# Passo 5: Análise a causa do cancelamento dos clientes

import pandas as pd #importando a bliblioteca do pandas como pd

tabela = pd.read_csv("cancelamentos_sample.csv") #declarando a tabela como uma variavel
tabela = tabela.drop(columns="CustomerID") #vai jogar fora a coluna customerID
tabela = tabela.dropna()
#print(tabela) #-> comando para visualizar a base de dados

#print(tabela["cancelou"].value_counts()) # Vai mostrar quantos cancelaram
#print(tabela["cancelou"].value_counts(normalize=True)) # Vai mostrar quantos cancelaram em %


