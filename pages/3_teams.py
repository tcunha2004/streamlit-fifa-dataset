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

# df filtrado pelo clube selecionado + index = name
df_filtered = df_data[df_data["Club"] == club].set_index("Name")

# clube logo + nome
url_club_logo = df_filtered.iloc[0]["Club Logo"]
response = requests.get(url_club_logo)
if response.status_code == 200:
    img = Image.open(BytesIO(response.content))
    st.image(img)
st.markdown(f"## {club}")

# colunas
columns = [
    "Age","Overall", "Value(£)",
    "Wage(£)", "Joined",
    "Height(cm.)", "Weight(lbs.)",
    "Contract Valid Until", "Release Clause(£)"
]

# dataframe filtrado por colunas selecionadas
st.dataframe(df_filtered[columns],
    column_config={
        "Overall": st.column_config.ProgressColumn(
            "Overall", format="%d" , min_value=0, max_value=100
        ),
        "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f",
                                                    min_value=0, max_value=df_filtered["Wage(£)"].max())
        # "Photo": st.column_config.ImageColumn(),
        # "Flag": st.column_config.ImageColumn("Country")
    }
)
