
import pyautogui
import pandas
import time

# pyautogui.click -> clicar
# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever
#pyautogui.hotkey("ctrl", "c")
#time.sleep(3)

pyautogui.PAUSE = 0.6

#Passo 1: Abrir o sistema da empresa
pyautogui.press("win")
pyautogui.write("chrome")

pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")


#Passo 2: Fazer logpin
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.write("CoderPro@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456789")
pyautogui.press("tab")
pyautogui.press("enter")

#Passo 3: Importar a base de dados dos produtos 
tabela=pandas.read_csv("produtos.csv")

#Passo 4: Cadastrar 1 produto
time.sleep(0.9)
for linha in tabela.index:
    pyautogui.press("tab")
    
    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preco-unitario
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    #tratamento de dados NAN 
    obs= str(tabela.loc[linha, "obs"]) #tratando como str para indentificar
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    contador = 0
    while contador < 8:
        contador += 1
        pyautogui.hotkey ("shift", "tab")
    