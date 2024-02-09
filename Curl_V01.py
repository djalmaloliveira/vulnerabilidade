#Script para ajustar arquivos do Tenable para Renomear arquivos log4j.jar
#Esta sendo criado um cmd para executar e renomear os arquivos
import os
from datetime import datetime

# Obter o caminho absoluto do arquivo
strPath ="D:\\Temp\\Vulnerabilidade\\Python"
strPathCasa ="D:\\Work\\Copel\\Python_Geral\\Enviar_Email"
strNomeFile = "vulnerabilities-01_31_2024_-09_14_52-gmt-3.csv"

path1 = os.path.join(strPath, strNomeFile)
pat3 = ""

# p482639,0012c3db-6f90-46d2-af47-121d5d46a572,"'
# The remote host is missing one of the following rollup KBs : 
#   - 5032189

#   - C:\windows\system32\ntoskrnl.exe has not been patched.
#     Remote version : 10.0.19041.3570
#     Should be      : 10.0.19041.3693

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
    strNewFile  = f'{strNewFile2}_Curl.cmd'
    #print  = f'1.Tam_Nome({int_SizeNome}) 2.Int_PosicaoVirgula: ({int_PosicaoVirgula}) 3.strPathNome ({strPathNome}) 1.NewFile2 ({strNewFile2}.cmd)'
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
            #print(pat2)
            if (len(pat2) > 6) :
                pat3 = pat2       
            if strLinha:
                if strLinha[slice(0, 10)] == "C:\Windows":
                    strLinha = strLinha.replace(':','$')                            
                    strLinha = (f'Dir \\\{pat3}\{strLinha} >>{strPath}\ListaVersaoCurl_{str_datahora}.txt')
                    strLinha = f'\n{strLinha}'
                    #print(strLinha)
                    fs.write(strLinha)                    
#print(str_datahora)
print(f'Nome do arquivo criado: {strNewNom2}')