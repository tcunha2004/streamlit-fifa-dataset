import streamlit as st
import requests
from io import BytesIO
from PIL import Image

# configs
st.set_page_config(
    page_title="Players",
    layout="wide"
)

# main df
df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index # all
club = st.sidebar.selectbox("Clube", clubes) # selected

# df filtrado por clube selecionado
df_players = df_data[df_data["Club"] == club]

players = df_players["Name"].value_counts().index # all
player = st.sidebar.selectbox("Jogador", players) # selected

# df filtrado pelo nome do jogador
player_stats = df_players[df_players["Name"] == player].iloc[0] # pega a primera aparição 

# foto + nome
url_player_img = player_stats["Photo"]
response = requests.get(url_player_img) 
if response.status_code == 200:
    img = Image.open(BytesIO(response.content))
    st.image(img)
st.title(player_stats["Name"])

# clube + posicao
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

# colunas
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100:.2f} m")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.2f} kg")
st.divider()

# Overall + progress bar
st.subheader(f"Overall - {player_stats["Overall"]}")
st.progress(int(player_stats["Overall"]))

# Metricas
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']}")
