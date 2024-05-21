import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV limpo
df = pd.read_csv('limpeza2.csv')

# Converter a coluna 'datetime' para datetime
df['datetime'] = pd.to_datetime(df['datetime'])

# Filtrar dados para um único dia
dia_especifico = '2024-04-22'
df_dia = df[df['datetime'].dt.date == pd.to_datetime(dia_especifico).date()]

# # Plotar gráfico de temperatura ao longo do dia específico
# plt.figure(figsize=(12, 6))
# plt.plot(df_dia['datetime'], df_dia['temperature'], label='Temperatura', color='r')
# plt.xlabel('Hora')
# plt.ylabel('Temperatura (°C)')
# plt.title(f'Temperatura em {dia_especifico}')
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.show()

# Gráfico de Temperatura e Umidade no Mesmo Dia
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.set_xlabel('Hora')
ax1.set_ylabel('Temperatura (°C)', color='r')
ax1.plot(df_dia['datetime'], df_dia['temperature'], label='Temperatura', color='r')
ax1.tick_params(axis='y', labelcolor='r')

ax2 = ax1.twinx()
ax2.set_ylabel('Umidade (%)', color='b')
ax2.plot(df_dia['datetime'], df_dia['humidity'], label='Umidade', color='b')
ax2.tick_params(axis='y', labelcolor='b')

plt.title(f'Temperatura e Umidade em {dia_especifico}')
fig.tight_layout()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
