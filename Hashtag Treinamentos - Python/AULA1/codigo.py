# Passo a passo do Projeto
# Passo 1 : Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2 : Fazer login
# Passo 3 : Importa a base de dados de produtos
# Passo 4 : Cadastrar o produto
# Passo 5 : Repetir o cadastro para todos os produtos

import pyautogui
import time
import pandas
tabela = pandas.read_csv("produtos.csv")

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> aperta 1 tecla
# pyautogui.hotkey -> atalho (combinação de teclas)

# pyautogui.press("win") -> Vai abrir a janelinha

# Passo 1

pyautogui.PAUSE = 1 # Adiciona um delay de 1 segundo

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(1) # Uma pausa maior para uma linha especifica


# Sessão de login
pyautogui.click(x=2465, y=-90)
pyautogui.write("email123@gmail.com")
pyautogui.press("tab")
pyautogui.write("123")
pyautogui.press("enter")

time.sleep(1)

for linha in tabela.index:

    pyautogui.click(x=2437, y=-180)

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]




    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(marca))
    pyautogui.press("tab")

    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    pyautogui.write(str(preco))
    pyautogui.press("tab")

    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
         pyautogui.write(str(obs))

    
    pyautogui.press("tab")
    pyautogui.press("enter") # apertar para enviar


# para dar scroll para cima-> pyautogui.scroll(500)
# para dar scroll para baixo-> pyautogui.scroll(-500)

