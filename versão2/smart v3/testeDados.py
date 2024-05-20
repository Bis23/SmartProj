import pandas as pd
import ast

# Carregar os dados CSV em um DataFrame
df = pd.read_csv('dados.csv')

# Definir uma função para extrair a temperatura de uma entrada
def ext_temp(entry):
    # Converter a string JSON em um dicionário Python
    data_dict = ast.literal_eval(entry)
    # Acessar e retornar a temperatura
    return data_dict['data_temperature']

def ext_humi(entry):
    data_dict = ast.literal_eval(entry)
    return data_dict['data_humidity']

# Aplicar a função extrair_temperatura em cada entrada da coluna 'fields' e criar uma nova coluna 'temperature'
df['temperature'] = df['fields'].apply(ext_temp)
df['humidity'] = df['fields'].apply(ext_humi)


plt.bar(range(len(df['temperature'])), df['temperature'], color='skyblue')
plt.ylim(24, 25)
plt.xlim(0, 1000)
plt.ylabel('Temperatura (°C)')
plt.title('Gráfico')
plt.show()

# Exibir a nova coluna 'temperature'
# print(df['humidity'])
