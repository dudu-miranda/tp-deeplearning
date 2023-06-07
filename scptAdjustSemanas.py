import csv
from datetime import datetime, timedelta
import sys

arq1 = sys.argv[1]
arq2 = sys.argv[2]
arq3 = sys.argv[3]

# Função para calcular a média de uma lista de números
def calcular_media(valores):
    return sum(valores) / len(valores)

# Ler o primeiro arquivo e obter as semanas
semanas = []
with open(arq1, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Pular o cabeçalho
    for row in reader:
        data_inicio = datetime.strptime(row[0], '%d/%m/%Y')
        data_fim = datetime.strptime(row[1], '%d/%m/%Y')
        semana = {
            'inicio': data_inicio.strftime('%d/%m/%Y'),
            'fim': data_fim.strftime('%d/%m/%Y'),
            'valores': []
        }
        semanas.append(semana)

# Ler o segundo arquivo e calcular as médias
with open(arq2, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Pular o cabeçalho
    for row in reader:
        data = datetime.strptime(row[0], '%d/%m/%Y')
        valor = float(row[1])
        for semana in semanas:
            data_inicio = datetime.strptime(semana['inicio'], '%d/%m/%Y')
            data_fim = datetime.strptime(semana['fim'], '%d/%m/%Y')
            if data_inicio <= data <= data_fim:
                semana['valores'].append(valor)
                break

# Calcular as médias e escrever em uma única linha
medias = [round(calcular_media(semana['valores']),4) for semana in semanas]

# Criar a linha de saída com valores separados por vírgula
linhas = [f"{semana['inicio']},{semana['fim']},{media}\n" for semana, media in zip(semanas, medias)]

# Escrever a linha em um novo arquivo
with open(arq3, 'w') as file:
    for linha in linhas:
        file.write(linha)

print("Script executado com sucesso!")

#python3 scptAdjustSemanas.py dados2/etanol_semanal_anp_blr.csv dados2/acucar_diario_ny_usd.csv dados2/acucar_diario_ny_usd_v2.csv