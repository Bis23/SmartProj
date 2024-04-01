import pandas as pd
import requests

def get_data(url):
    response = requests.get(url, verify=False)
    data = response.json()
    return data

api_url = "https://smartcampus-k8s.maua.br/api/timeseries/v0.1/smartcampusmaua/SmartLights?interval=20"
data = get_data(api_url)

df = pd.DataFrame(data)
print(df)

# colunas: fields, name, tags, timestamp