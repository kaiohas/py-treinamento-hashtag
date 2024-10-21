import streamlit as st
import pandas as pd
import yfinance as yf

acoes = ['ITUB4.SA','ABEV3.SA','PETR4.SA','VALE3.SA','SBSP3.SA','BBDC4.SA','VIVA3.SA','CMIG4.SA']

# Criar as funções de carregamentos de dados
    #Cotações do Itau - ITUB4 - 2010 a 2024
#BAS.DE - BASF

@st.cache_data
def carregar_dados(empresas):
    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers)
    cotacoes_acao = dados_acao.history(period='1d',start='2010-01-01',end='2024-01-01')
    cotacoes_acao = cotacoes_acao['Close']
    return cotacoes_acao

dados = carregar_dados(acoes)


# Criar uma interface do Streamlit

st.write("""
# App preços de ações
O grafico abaixo representa a evolução do preço das ações ao longo dos anos
""")


# Preparar as visualizações
lista_acoes = st.multiselect("Escolha as ações para visualizar",dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: 'Close'})




# Criar grafico
st.line_chart(dados)

st.write("""
# Fim do APP
""")