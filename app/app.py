import streamlit as st
import os
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from utils.dadosfera import Dadosfera

from utils.tools import create_pandas_df

st.set_page_config(
    page_icon="https://s3.amazonaws.com/gupy5/production/companies/1286/career/2122/images/2022-01-05_13-07_logo.png",
    page_title="Início",
    layout="wide",
)
st.sidebar.image(
    "https://cdn-images-1.medium.com/max/1200/1*OPrCFbKQFOeL0QKCuDeR1g.png", width=300
)


st.markdown(
    "[Componentes Streamlit](https://docs.streamlit.io/library/api-reference)")

with st.sidebar.expander("Carregue o arquivo", expanded=True):
    uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    uploaded_df = pd.read_csv(uploaded_file)

    uploaded_df.to_csv("arquivo_local.csv", index=False)

local_file = "arquivo_local.csv"

if os.path.exists(local_file):
    print("O arquivo existe.")
    df = pd.read_csv(local_file)

    # st.markdown("Verificar as primeiras linhas do dataframe")
    # st.dataframe(df.head(), use_container_width=True)

    # st.markdown("Verificar estatísticas descritivas das colunas numéricas")
    # st.dataframe(df.describe(), use_container_width=True)

    # st.markdown("Verificar a contagem de valores únicos em cada coluna")
    # st.dataframe(df.nunique(), use_container_width=True)

    fig = px.histogram(df, x="Age", nbins=20, title="Distribuição da Idade")
    # st.plotly_chart(fig, use_container_width=True)

    fig = px.bar(df, x="Department",
                 title="Contagem de Funcionários por Departamento")
    # st.plotly_chart(fig, use_container_width=True)

    # Verificar a relação entre o tempo total de trabalho (coluna TotalWorkingYears) e o nível do cargo (coluna JobLevel)
    fig = px.scatter(
        df,
        x="TotalWorkingYears",
        y="JobLevel",
        color="Department",
        title="Relação entre Tempo Total de Trabalho e Nível do Cargo",
    )
    # st.plotly_chart(fig, use_container_width=True)

    # Correlação entre Variáveis Numéricas
    correlation_matrix = df.select_dtypes(include=np.number).corr()
    fig_correlation = go.Figure(
        data=go.Heatmap(
            z=correlation_matrix.values,
            x=correlation_matrix.columns,
            y=correlation_matrix.columns,
            colorscale="Viridis",
        )
    )
    fig_correlation.update_layout(title="Correlação entre Variáveis Numéricas")

    # st.plotly_chart(fig_correlation)
