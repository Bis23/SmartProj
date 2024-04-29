import pandas as pd
import requests
import matplotlib.pyplot as plt

api_url = "https://smartcampus-k8s.maua.br/api/timeseries/v0.1/smartcampusmaua/SmartLights?interval=20"
data = get_data(api_url)
df = pd.DataFrame(data)

def get_data(url):
    response = requests.get(url, verify=False)
    data = response.json()
    return data

# Lista do campo: Fields
def extrair_temperatura(df):
    df2 = df['fields'].apply(pd.Series)
    return df2['data_temperature'].tolist()

def extrair_umidade(df):
    df2 = df['fields'].apply(pd.Series)
    return df2['data_humidity'].tolist()



# Extrair dados de temperatura e umidade usando as funções separadas
lista_temperatura = extrair_temperatura(df)
lista_umidade = extrair_umidade(df)