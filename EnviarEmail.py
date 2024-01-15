#
#Enviar Email
# Tratar arquivos

import csv
import os


# Obter o caminho absoluto do arquivo
path1 = os.path.join("d:\\Work\\Copel\\Python_Geral\\Enviar_Email", "vulnerabilities-01_12_2024_-18_39_05-gmt-3.csv")

def extrairPat(texto):
    tam = len(str(texto))
    str1 = str(texto)[2:tam-2]    
    #print(f"{tam}-Patrimonio: {str1} ")

def extrairFile(texto):    
    texto = str(texto)
    texto = texto.replace("Fixed version     : 2.12.2", "**")
    texto = texto.replace("Fixed version     : 2.12.4", "**")
    texto = texto.replace("Fixed version     : 2.15.0", "**")
    texto = texto.replace("Fixed version     : 2.16.0", "**")
    texto = texto.replace("Fixed version     : 2.17.0", "**")
    texto = texto.replace("Fixed version     : 2.17.1", "**")
    texto = texto.replace("Fixed version     : 2.12.3 / 2.17.0", "**")
    texto = texto.replace("Installed version : 2.8.2", "**")
    texto = texto.replace("Installed version : 1.2.16", "**")
    texto = texto.replace("Installed version : 1.2.13", "**")
    texto = texto.replace("Installed version : 1.2.11", "**")
    texto = texto.replace("Installed version : 1.2.14", "**")
    texto = texto.replace("Installed version : 1.2.15", "**")
    texto = texto.replace("Installed version : 1.2.16", "**")
    texto = texto.replace("Installed version : 1.2.17", "**")
    texto = texto.replace("Installed version : 2.11.1", "**")
    texto = texto.replace("Installed version : 2.12.4", "**")
    texto = texto.replace("Installed version : 2.14.0", "**")
    texto = texto.replace("C:", "C$")
    texto = texto.replace("D:", "D$")
    texto = texto.replace("E:", "E$")
    
    

    texto = texto.replace("  Path              : ", "**")
    
    print(texto)
          
with open(path1, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    contador = 0
    for row in reader:
        contador = contador + 1
        tamanho = len(row)
        patrimonio = row[1:2]
        id = row[2:3]
        texto = row[3:4]
        #print (f"Numero: {contador} -- Pat({patrimonio}) -- texto({texto}) ")
        extrairPat(patrimonio)
        extrairFile(texto)

        
