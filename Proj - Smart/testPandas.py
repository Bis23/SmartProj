import pandas as pd
import requests
import matplotlib.pyplot as plt

def get_data(url):
    response = requests.get(url, verify=False)
    data = response.json()
    return data

api_url = "https://smartcampus-k8s.maua.br/api/timeseries/v0.1/smartcampusmaua/SmartLights/deviceId/0004a30b00e94a9d"
data = get_data(api_url)

df = pd.DataFrame(data)
print(df)

# colunas: fields, name, tags, timestamp
# print(df['fields'].apply(lambda x: x['data_humidity']))
