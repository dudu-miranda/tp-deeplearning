
import sys
arq = sys.argv[1]

with open(arq, 'r') as arquivo_origem:
    linhas = arquivo_origem.readlines()
    linhas_invertidas = linhas[::-1]
    
with open(arq, 'w') as arquivo_destino:
    arquivo_destino.writelines(linhas_invertidas)
