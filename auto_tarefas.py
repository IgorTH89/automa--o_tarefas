# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui 
import time
pyautogui.PAUSE = 0.5

#Abrir o navegador:
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

#Entrar no link:
time.sleep(4)
pyautogui.click(x=441, y=47)
pyautogui.press("delete")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=951, y=383)
pyautogui.write("igorprojects@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
# Passo 3: Importar a base de dados
import pandas as pd

tabela = pd.read_csv("C:/Users/igort/Documents/Estudos/Cursos/Python/jornada_python/automação_tarefas/produtos.csv")
print(tabela)  

# Passo 4: Cadastrar os produtos
for linha in tabela.index:
    # codigo    Hashtag 
    pyautogui.click(x=980, y=284)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim