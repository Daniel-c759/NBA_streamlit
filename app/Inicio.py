import streamlit as st

st.set_page_config(
    page_title="NBA stats"
)

st.header("Bienvenido a la página de estadísticas de la NBA :smile:")

st.markdown(""" ## ¿Qué encuentras aquí?
En esta página encuentras información sobre los partidos de la 
NBA desde la temporada 2003-2004, utilizando información disponible en
kaggle en la [base de datos NBA](https://www.kaggle.com/datasets/nathanlauga/nba-games).

La página es construida con streamlit como un desarrollo multiapp y 
cuenta con la siguiente estructura:

* Jugadores: En ésta encuentas información disponible de los jugadores que hayan 
participado en alguna temporada desde la campaña 2003-2004. Adicionalmente se puede comparar 
las estadísticas de dos jugadores.

* Equipos: En ésta encuentras información de los equipos y sus jugadores para 
una temporada especifica.
""")