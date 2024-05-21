import pandas as pd
from datetime import datetime

# Carregar os dados CSV em um DataFrame
df = pd.read_csv('dados.csv')

# Converter timestamps Unix em objetos de datetime
df['datetime'] = pd.to_datetime(df['timestamp'], unit='ns')

# with open('tempos.txt', 'w') as file:
#     # Iterar sobre os elementos da lista
#     for item in df['datetime']:
#         # Escrever uma linha de texto para cada instância
#         file.write(f'{item}\n')

print(df['datetime'])