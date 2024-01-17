#
#Enviar Email
#Tratar arquivos

import csv
import os

#path1 = os.path.join("d:\\Work\\Copel\\Python_Geral\\Enviar_Email", "vulnerabilities-01_12_2024_-18_39_05-gmt-3.csv")
path1 = os.path.join("D:\\Temp\\Vulnerabilidade\\Log4J", "vulnerabilities-01_16_2024_-15_34_24-gmt-3_V1.csv")
#path1 = os.path.join("D:\\Temp\\Vulnerabilidade\\Log4J", "PontosCardeais.txt")


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
    texto = texto.replace("Installed version : 2.12.1", "**")
    texto = texto.replace("Installed version : 2.14.0", "**")    
    texto = texto.replace("C:", "C$")
    texto = texto.replace("D:", "D$")
    texto = texto.replace("E:", "E$")    
    texto = texto.replace("  Path              : ", "**")
    texto = texto.replace("**", "")
    texto = texto.replace("\\n", "")
    texto = texto.replace("]", "")
    #texto = texto.replace("/]", "++")
    qtosJar = texto.count(".jar")
    
    #print(f"Quantos Jar = {qtosJar} Texto:{texto}")    
    #print(texto.splitlines())
    return texto

arqSaida = "Saida22.txt"

if os.path.exists(arqSaida):
    os.remove(arqSaida)

# adiciona uma informação ao texto original
with open(arqSaida, "a") as saida22:          
    with open(path1, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        contador = 0
        for row in reader:
            contador = contador + 1
            tamanho = len(row)
            patrimonio = row[0:1]
            id = row[2:3]
            texto = row[2:3]
            texto = (f"{patrimonio} -- {texto} ")
            texto = extrairFile(texto)              
            texto = (f"\n{texto}")            
            print (texto)

            #saida22.write(texto)
            saida22.writelines(texto)
            #extrairPat(patrimonio)
        


        

