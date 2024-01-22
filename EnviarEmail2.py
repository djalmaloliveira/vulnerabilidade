#Enviar Email
# Tratar arquivos
import os

# Obter o caminho absoluto do arquivo
path1 = os.path.join("d:\\Work\\Copel\\Python_Geral\\Enviar_Email", "vulnerabilities-01_12_2024_-18_39_05-gmt-3_V1.csv")
pat3 = ""

def Patrimonio(linha):
    # 10.238.17.201,p489857,fe181f99-0129-4d8b-9df3-a4a79a752135    
    pat = ""
    primeiraVirgula = linha.find(",")
    segundavirgula = linha[primeiraVirgula+8:primeiraVirgula+9]
    
    if (primeiraVirgula > 10 and primeiraVirgula < 20 ):
        pat = linha[primeiraVirgula+1:primeiraVirgula+8]   
        #print(f'PrimeiraVirgula: {primeiraVirgula} SegundaVirgula {segundavirgula} Pat: {pat} Linha: ({linha})')
    return pat
def pegaFiles(caminho):
    qtasBarras = caminho.count('\\')
    print(f'Caminho: qtasBarras {qtasBarras} -  {caminho}')

def Path(linha):
    posicaoPath = linha[2:6]
    if posicaoPath == 'Path':     
        tamanhoPath = len(linha)
        caminho = linha[22:22+(tamanhoPath-23)]
        pegarfile = pegaFiles(caminho)
        #print(f'posição: ({posicaoPath}) caminho ({caminho})  linha {linha}')

with open(path1, "r", encoding="utf-8") as f:
    contador = 0
    arquivo = f.readlines()
    for linha in arquivo:
        contador = contador + 1
        
        pat2 = Patrimonio(linha)
        tamanhoPat2 = len(pat2)
        
        if tamanhoPat2 > 6:
            pat3 = pat2       
        
        Path(linha)
        
       # print(f'Linha({contador}): Pat3 {pat3} -- tamanhopat2 {tamanhoPat2}-- {linha}')
        

    
