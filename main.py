import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()


API_KEY=os.getenv("API_KEY")
SHEET_ID=os.getenv("SHEET_ID")
SHEET_NAME= os.getenv("SHEET_NAME")

def get_movies():
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}/values/{SHEET_NAME}?key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data["values"][1:]

style = """
<style>
[data-testid="stAppViewContainer"]
{
    background-color: black !important;
}
</style>
"""

st.markdown(style, unsafe_allow_html=True)

general_header = """
<h1 style="color: darkgreen; font-size:3rem;">{}</h1>
"""

movie_header = """
<h1 style="color: #C1C1C1; font-size:2rem;">{}</h1>
"""


st.markdown(general_header.format("Favori Diziler"), unsafe_allow_html=True)

# list of favorite series
series = get_movies()

# display series
for serie in series:
    st.markdown(movie_header.format(serie[0]), unsafe_allow_html=True)
    st.image(serie[1])
    
    


