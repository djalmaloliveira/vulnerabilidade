#Script para ajustar arquivos do Tenable para Renomear arquivos log4j.jar
#Esta sendo criado um cmd para executar e renomear os arquivos
import os
from datetime import datetime

# Obter o caminho absoluto do arquivo
strPath ="D:\\Temp\\Vulnerabilidade\\Python"
strPath ="D:\\Temp\\Vulnerabilidade\\Curl"
strPathCasa ="D:\\Work\\Copel\\Python_Geral\\Enviar_Email"
strNomeFile = "vulnerabilities-01_26_2024_-16_17_30-gmt-3.csv"

path1 = os.path.join(strPath, strNomeFile)
pat3 = ""

# Exemplo de estrutura do arquivo fonte
# p489544,0104ed78-7176-4d81-b799-e3d2879a0447,"'
#   Path              : C:\APL\SigepWEB\sigepcliente\lib\log4j-1.2.16.jar
#   Installed version : 1.2.16
#   Fixed version     : 2.16.0
# "
if os.path.exists(path1):
    print("A arquivo Existe !")
else:
    print("Arquivo Não existe")

def Patrimonio(linha):
    # p489857,fe181f99-0129-4d8b-9df3-a4a79a752135    
    pat = ""    
    primeiraVirgula = linha.find(",")    
    if (primeiraVirgula > 6 and primeiraVirgula < 15):
        pat = linha[0:primeiraVirgula]  
        #print(f'3-PrimeiraVirgula: ({primeiraVirgula}) Pat: ({pat}) Linha: ({linha})')
    return pat


def Path(linha):
    posicaoPath = linha[2:6]
    if posicaoPath == 'Path':     
        tamanhoPath = len(linha)
        caminho = linha[22:22+(tamanhoPath-23)]
        #print(f'posição: ({posicaoPath}) caminho ({caminho})  linha {linha}')
        return(caminho)

def NomeCMD(strPathNome):        
    int_PosicaoVirgula = strNomeFile.rfind('.csv')
    strNewFile2 = strPathNome[0:int_PosicaoVirgula]    
    strNewFile  = f'{strNewFile2}.cmd'
    #print  = f'1.Tamanho_Nome({int_SizeNome}) 2.Int_PosicaoVirgula: ({int_PosicaoVirgula}) 3.strPathNome ({strPathNome}) 1.NewFile2 ({strNewFile2}.cmd)'
    print(strNewFile)
    return(strNewFile)

strNewNom2 = NomeCMD(strNomeFile)
str_datahora = datetime.now().strftime('%d%m%Y%H%M%S')

with open(strNewNom2, "w", encoding="utf-8") as fs:
        
    with open(path1, "r", encoding="utf-8") as f:
        contador = 0
        arquivo = f.readlines()
        for linha in arquivo:
            contador = contador + 1
            
            pat2 = Patrimonio(linha)            
            strLinha = Path(linha)                        
            #strLinha = extrairFile(strLinha2) 
            if (len(pat2) > 6) :
                pat3 = pat2       
            if type(strLinha) == str :
                strLinha = (f'Dir \\\{pat3}\{strLinha} >>Lista_Curl_{str_datahora}.txt')
                #print(f'1.Linha({contador});3.linha;Ren "\\\{pat3}{strLinha}')
                strLinha = strLinha.replace(':','$')
                strLinha = f'\n{strLinha}'                
                fs.write(strLinha)
                print(strLinha)



#print(str_datahora)
print(f'Nome do arquivo criado: {strNewNom2}')