import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados com caching atualizado
@st.cache_data
def load_data():
    df = pd.read_csv('limpeza.csv')
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

df = load_data()

# Título e descrição do site
st.title('Monitoramento Climático')
st.markdown('### Visualização de Dados de Temperatura e Umidade')

# Seleção de filtro de data
st.sidebar.header('Filtros')
start_date = st.sidebar.date_input('Data inicial', df['datetime'].min().date())
end_date = st.sidebar.date_input('Data final', df['datetime'].max().date())

# Filtragem de dados
mask = (df['datetime'].dt.date >= start_date) & (df['datetime'].dt.date <= end_date)
df_filtered = df[mask]

# Gráfico de temperatura
st.header('Gráfico de Temperatura')
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df_filtered['datetime'], df_filtered['temperature'], color='r', label='Temperatura')
ax.set_xlabel('Data e Hora')
ax.set_ylabel('Temperatura (°C)')
ax.set_title('Temperatura ao longo do tempo')
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Gráfico de umidade
st.header('Gráfico de Umidade')
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df_filtered['datetime'], df_filtered['humidity'], color='b', label='Umidade')
ax.set_xlabel('Data e Hora')
ax.set_ylabel('Umidade (%)')
ax.set_title('Umidade ao longo do tempo')
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Estatísticas Resumidas
st.header('Estatísticas Resumidas')
st.write(df_filtered.describe())

# Exportar dados filtrados
st.header('Exportar Dados Filtrados')
st.write('Clique no botão abaixo para baixar os dados filtrados.')
csv = df_filtered.to_csv(index=False).encode('utf-8')
st.download_button(label="Baixar CSV", data=csv, file_name='dados_filtrados.csv', mime='text/csv')
