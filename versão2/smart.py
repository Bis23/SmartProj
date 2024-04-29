import pandas as pd
import requests
import matplotlib.pyplot as plt

def get_data(url):
    response = requests.get(url, verify=False)
    data = response.json()
    return data

api_url = "https://smartcampus-k8s.maua.br/api/timeseries/v0.1/smartcampusmaua/SmartLights?interval=20"
data = get_data(api_url)

df = pd.DataFrame(data)
# print(df.describe())

df_foda = df['fields'].apply(pd.Series)
data_temperature = df_foda['data_temperature']
# print(data_temperature)

df_foda = df['fields'].apply(pd.Series)
data_humidity = df_foda['data_humidity']
# print(data_humidity)

lista_temperatuta = []
for i in data_temperature:
    lista_temperatuta.append(i)
# print(lista_temperatuta)

lista_humidade = []
for i in data_humidity:
    lista_humidade.append(i)
# print(lista_humidade)

# colunas: fields, name, tags, timestamp

plt.bar(lista_humidade, lista_temperatuta, width = 1)
# Adicionar rótulos aos eixos e título
plt.ylabel('Temperatura')
plt.xlabel('Humidade')
plt.title('Temp x Humidade')
# Mostrar o gráfico
plt.show()

# Construção do histograma