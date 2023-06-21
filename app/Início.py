import streamlit as st
import plotly.express as px
import pandas as pd
from utils.dadosfera import Dadosfera

from utils.tools import create_pandas_df

st.set_page_config(
    page_icon="https://s3.amazonaws.com/gupy5/production/companies/1286/career/2122/images/2022-01-05_13-07_logo.png",
    page_title="Início",
    layout="centered",
)
st.sidebar.image(
    "https://cdn-images-1.medium.com/max/1200/1*OPrCFbKQFOeL0QKCuDeR1g.png", width=300
)


st.markdown("[Componentes Streamlit](https://docs.streamlit.io/library/api-reference)")
