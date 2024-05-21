# SmartProj
#### Projeto em desenvolvimento com o SmartCampusMaua, no intuito de fornecer uma forma mais simples e limpa para visualização de dados. Para essa demonstração, utilizamos o banco de dados do SmartLights.

Para rodar o site, siga o passo a passo a seguir:
1. Certifique de que as seguintes bibliotecas estejam **instaladas**:  
   `pip install streamlit`  
   `pip install pandas`  
   `pip install matplotlib.pyplot`  
   `pip install virtualenv`  

2. Vá para o diretório em que o arquivo *"testeStream.py"* se encontra e crie um novo ambiente virtual:  
   `virtualenv nome_da_virtualenv`

3. **Ative** o ambiente virtual que você criou:
   * No ambiente *Linux ou macOS*: `source nome_da_virtualenv/bin/activate`
   * No ambiente *Windows*: `nome_da_virtualenv/Scripts/Activate`  
  
4. **Rode o site** com o seguinte comando no terminal:  
   `streamlit run testeStream.py`

5. Acesse o app Streamlit com o link que aparecer no terminal.  
  
  
#### Documentações utilizadas:
- [StreamLit](https://streamlit.io/)
- [SmartLights](https://github.com/OpenDataTelemetry/timeseries-api)
- [SmartLights - Documentação](https://github.com/SmartCampusMaua/Docs/tree/doc/analytics/Tools/Analytics/Pandas)
