import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV limpo
df = pd.read_csv('limpeza2.csv')

# Converter a coluna 'datetime' para datetime
df['datetime'] = pd.to_datetime(df['datetime'])

# Filtrar dados para o mês de abril do ano específico
ano_especifico = 2024
mes_especifico = 5
df_mes = df[(df['datetime'].dt.year == ano_especifico) & (df['datetime'].dt.month == mes_especifico)]

# Exibir as primeiras linhas dos dados filtrados
print(df_mes.head())

# Salvar os dados filtrados em um novo arquivo CSV
df_mes.to_csv('dados_mes_abril.csv', index=False)

# Plotar gráfico de temperatura ao longo do mês de abril
# plt.figure(figsize=(12, 6))
# plt.plot(df_mes['datetime'], df_mes['temperature'], label='Temperatura', color='r')
# plt.xlabel('Data e Hora')
# plt.ylabel('Temperatura (°C)')
# plt.title(f'Temperatura em Abril {ano_especifico}')
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.show()

# Gráfico de Temperatura e Umidade no Mês de Abril
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.set_xlabel('Data e Hora')
ax1.set_ylabel('Temperatura (°C)', color='r')
ax1.plot(df_mes['datetime'], df_mes['temperature'], label='Temperatura', color='r')
ax1.tick_params(axis='y', labelcolor='r')

ax2 = ax1.twinx()
ax2.set_ylabel('Umidade (%)', color='b')
ax2.plot(df_mes['datetime'], df_mes['humidity'], label='Umidade', color='b')
ax2.tick_params(axis='y', labelcolor='b')

plt.title(f'Temperatura e Umidade em Abril {ano_especifico}')
fig.tight_layout()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
