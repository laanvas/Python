# Python IA

# Passo a Passo:
# Passo 0 - Entender o desafio e a empresa
# Passo 1 - Importar a base de dados
# Passo 2 - Preparar a base de dadoss para a inteligencia artificial
# Passo 3 - Criar o modela de IA -> Score crédito: Good, Standard, Poor
# Passo 4 - Escolher o melhor modelo
# Passo 5 - Fazer novas previsões

# Existem centenas de modelos de IA

import pandas as pd

tabela = pd.read_csv("clientes.csv")

# Verificar se a gente tem algum valor vazio

# As IA so conseguem trabalhar com numeros

# Label Encoder = Transforma os valores em numero

# Ta importando o LabelEncoder
from sklearn.preprocessing import LabelEncoder

codificador = LabelEncoder()
tabela["profissao"] = codificador.fit_transform(tabela["profissao"])
tabela["mix_credito"] = codificador.fit_transform(tabela["mix_credito"])
tabela["comportamento_pagamento"] = codificador.fit_transform(tabela["comportamento_pagamento"])

# o y são os dados que você quer prevê
y = tabela["score_credito"]
colunas = ["score_credito", "id_cliente"]
x = tabela.drop(columns = colunas)

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)


# arvore de decisão
from sklearn.ensemble import RandomForestClassifier
# vizinhos proximos
from sklearn.neighbors import KNeighborsClassifier

modelo_arvoredecisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

modelo_arvoredecisao.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)

from sklearn.metrics import accuracy_score

# declaração de variaveis
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste.to_numpy())
previsao_knn = modelo_knn.predict(x_teste.to_numpy())

# vai mostrar o resultado
print(accuracy_score(y_teste, previsao_arvoredecisao))
print(accuracy_score(y_teste, previsao_knn))

