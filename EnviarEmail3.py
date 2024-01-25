#Enviar Email
# Tratar arquivos
import os

# Obter o caminho absoluto do arquivo
path1 = os.path.join("d:\\Work\\Copel\\Python_Geral\\Enviar_Email", "vulnerabilities-01_12_2024_-18_39_05-gmt-3_V1.csv")
path1 = os.path.join("D:\\Temp\\Vulnerabilidade\\Python\\EnviarEmail2", "vulnerabilities-01_22_2024_-15_15_57-gmt-3_V1.csv")
path1 = os.path.join("D:\\Temp\\Vulnerabilidade\\Python", "vulnerabilities-01_25_2024_-10_18_01-gmt-3.csv")
pat3 = ""

# Exemplo de estrutura do arquivo fonte
# p489544,0104ed78-7176-4d81-b799-e3d2879a0447,"'
#   Path              : C:\APL\SigepWEB\sigepcliente\lib\log4j-1.2.16.jar
#   Installed version : 1.2.16
#   Fixed version     : 2.16.0
# "
if os.path.exists(path1):
    print("A arquivo Existe !")

def Patrimonio(linha):
    # p489857,fe181f99-0129-4d8b-9df3-a4a79a752135    
    pat = ""    
    primeiraVirgula = linha.find(",")    
    if (primeiraVirgula > 6 and primeiraVirgula < 15):
        pat = linha[0:primeiraVirgula]  
        #print(f'3-PrimeiraVirgula: ({primeiraVirgula}) Pat: ({pat}) Linha: ({linha})')
    return pat

def pegaFiles(caminho):    
    tamstring = len(caminho)  
    localbarra = linha.rfind("\\") 
    inicioString = localbarra - 21
    strFile = caminho[inicioString:tamstring]
    caminho = caminho.replace(":\\","$\\")    
    caminho = f'\\{caminho}"'
    strFiles = (f'{caminho} {strFile}_old')
    #print(f'2 - LocalBarra: {localbarra}- InicioString {inicioString} - TamanhoString {tamstring} - corte: {caminho} Recorte: {strFile}')    
    #print(strFiles)
    return strFiles

def Path(linha):
    posicaoPath = linha[2:6]
    if posicaoPath == 'Path':     
        tamanhoPath = len(linha)
        caminho = linha[22:22+(tamanhoPath-23)]
        pegarfile = pegaFiles(caminho)
        #print(f'posição: ({posicaoPath}) caminho ({caminho})  linha {linha}')
        return(pegarfile)
#with open('Saida2.cmd', "a", encoding="utf-8") as fs:


#nome = "João2"
arquivo = open("nome.txt", "w")
#arquivo.write(nome)
#arquivo.close()

with open(path1, "r", encoding="utf-8") as f:
    #arquivo.write(path1)
    #arquivo.close
    contador = 0
    arquivo = f.readlines()
    for linha in arquivo:
        contador = contador + 1
        
        pat2 = Patrimonio(linha)
        pegaFile = pegaFiles(linha)        
        strLinha = Path(linha)        
        
                
        if (len(pat2) > 6) :
            pat3 = pat2       
        if type(strLinha) == str :
            strLinha = (f'Ren "\\\{pat3}{strLinha}')
            #print(f'1.Linha({contador});3.linha;Ren "\\\{pat3}{strLinha}')

            
            print(strLinha)
        
