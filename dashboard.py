import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")
st.title("SampaTransit - Operação em Tempo Real")

path = "sptrans_gold"
if not os.path.exists(path) or not os.listdir(path):
    st.warning("Aguardando dados da camada Gold...")
    st.stop()

df = pd.read_parquet(path)

ultima_extracao_utc = pd.to_datetime(df['extracted_at'].max())
if ultima_extracao_utc.tz is None:
    ultima_extracao_utc = ultima_extracao_utc.tz_localize('UTC')
ultima_extracao_br = ultima_extracao_utc.tz_convert('America/Sao_Paulo')

df_atual = df[df['extracted_at'] == df['extracted_at'].max()]

linha = st.sidebar.selectbox("Filtro de Linha", ["Todas"] + list(df_atual['codigo_linha'].unique()))
if linha != "Todas":
    df_atual = df_atual[df_atual['codigo_linha'] == linha]

col1, col2, col3 = st.columns(3)
col1.metric("Veículos Ativos", len(df_atual))

if 'velocidade' in df_atual.columns:
    col2.metric("Velocidade Média", f"{df_atual['velocidade'].mean():.1f} km/h")
else:
    col2.metric("Linhas Operando", df_atual['codigo_linha'].nunique())

col3.metric("Atualização", ultima_extracao_br.strftime('%H:%M:%S'))

st.map(df_atual[['latitude', 'longitude']])