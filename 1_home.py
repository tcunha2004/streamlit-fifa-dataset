import streamlit as st
import pandas as pd
import datetime

# configs
st.set_page_config(
    page_title="Players",
    layout="wide"
)

if "data" not in st.session_state: # caso nao tenha um "data" na sessão
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0) # qual coluna vai servir de indice
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.datetime.today().year] # filtra apenas os que tem contrato ativo
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False) # ordenar
    st.session_state["data"] = df_data

st.markdown("# FIFA 2023 OFFICIAL DATASET")

st.sidebar.markdown("Desenvolvido por Thiago Cunha")

st.html(
    """
    <style>
        .btn{
            border:1px solid black; 
            background:white;
            color: black;
        }
        .btn:active{

        }
        .btn-img{
            height: 40px;
        }
    </style>
    <a href="https://github.com/tcunha2004" target="_blank">
        <button class="btn">
            <img src="https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png" alt="github" class="btn-img"/>
            <span>Github</span>
        </button>
    </a>
    """
)

st.markdown(
    """
        O conjunto de dados
        de jogadores de futebol de 2023 fornece informações
        abrangentes sobre jogadores de futebol profissionais.
        O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos
        do jogador, características físicas, estatísticas de jogo, detalhes do contrato e
        afiliações de clubes.

        Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para
        analistas de futebol, pesquisadores e entusiastas interessados em explorar vários
        aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de
        desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e
        desenvolvimento do jogador ao longo do tempo.
    """
)