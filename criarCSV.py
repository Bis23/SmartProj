import pandas as pd
import requests

def get_data(url):
    response = requests.get(url, verify=False)
    data = response.json()
    return data

def save_data_to_csv(api_url, filename):
    data = get_data(api_url)
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)  # Index=False para não salvar o índice no arquivo CSV
    print("Dados salvos em", filename)

# URL da API
api_url = "https://smartcampus-k8s.maua.br/api/timeseries/v0.1/smartcampusmaua/SmartLights/deviceId/0004a30b00e94a9d"

# Nome do arquivo CSV para salvar os dados
nome_arquivo_csv = "dados.csv"

# Salva os dados em um arquivo CSV
save_data_to_csv(api_url, nome_arquivo_csv)
