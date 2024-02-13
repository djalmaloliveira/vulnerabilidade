#Script para ajustar arquivos do Tenable para Renomear arquivos log4j.jar
#Esta sendo criado um cmd para executar e renomear os arquivos
import os

# Obter o caminho absoluto do arquivo
strPath ="D:\\Temp\\Vulnerabilidade\\Python"
strPath ="D:\\Work\\Copel\\Python_Geral\\Enviar_Email\\vulnerabilidade-main"
strNomeFile = "ListaVersaoCurl_30012024172520.txt"

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
    #print(linha)
    primeiraVirgula = linha.find("Windows")   
    if (primeiraVirgula > 20 and primeiraVirgula < 30):
        pat = linha[12:19]  
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

def StrSizeFile(linha):    
    strArquivo = linha.rfind("arquivo(s)") 
    if strArquivo == 17:        
        strSize = linha[35:42]        
        #print(f'1.Arquivo {strArquivo} 2.Size:({strSize}) 3.linha {linha}')
        return(strSize)

def extrairFile(texto):    
    texto = str(texto)
    texto = texto.replace("Automa‡Ćo", "Automação")
    texto = texto.replace("SASE", "SASE_NaoApagar")
    texto = texto.replace("SigepWEB", "SigepWEB_NaoApagar")    
    texto = texto.replace("‡Æo", "ção")
    texto = texto.replace("Æ", "ã")
    
    return(texto)

def NomeCMD(strPathNome):    
    int_PosicaoVirgula = strNomeFile.rfind('.txt')
    strNewFile2 = strPathNome[0:int_PosicaoVirgula]
    strNewFile  = f'{strNewFile2}_Dir.cmd'
    #print  = f'1.Tamanho_Nome({int_SizeNome}) 2.Int_PosicaoVirgula: ({int_PosicaoVirgula}) 3.strPathNome ({strPathNome}) 1.NewFile2 ({strNewFile2}.cmd)'
    print(strNewFile)
    return(strNewFile)

strNewNom2 = NomeCMD(strNomeFile)
#print(path1)
with open(strNewNom2, "w", encoding="utf-8") as fs:
        
    with open(path1, "r") as f:
        contador = 0
        arquivo = f.readlines()
        for linha in arquivo:
            contador = contador + 1
            
            pat2 = Patrimonio(linha)
            pegaFile = pegaFiles(linha)        
            strLinha = Path(linha)                        
            strSize  = StrSizeFile(linha)
            strLinha = Path(linha)                        
            #strLinha = extrairFile(strLinha2) 
            
            if (len(pat2) > 6) :
                pat3 = pat2       
            #print(f'1.Linha({contador}) 2.strSize {strSize};3.linha;"\\\{pat3}{strLinha}')                
            if type(strSize) == str :
                strLinha = (f'Tamanho "\\\{pat3}\\{strSize}')
                #print(f'1.Linha({contador});3.linha;Ren "\\\{pat3}{strLinha}')
                strLinha = f'\n{strLinha}'
                strLinha2 = extrairFile(strLinha)
                fs.write(strLinha2)
                print(strLinha2)
            
print(f'Nome do arquivo criado: {strNewNom2}')