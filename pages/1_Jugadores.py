import mysql.connector as connection
import pandas as pd
import streamlit as st
import funciones.players as players
import os

host=os.environ.get("host")
usuario=os.environ.get("user")
contraseña=os.environ.get("passwd")
base_datos=os.environ.get("db")


NBA=connection.connect(
    host="localhost",
    user="root",
    passwd="daniel97",
    db="NBA"
)

st.header(":runner: Jugadores")

st.markdown("""
Aquí podras ver el aporte del jugador que desees a sus equipos, solo selecciona un jugador 
o escribe el nombre/apellido de él abajo :point_down:
""")

jugadores_query=f"""
select distinct PLAYER_NAME as jugador
from NBA.games_details
order by jugador desc
"""

jugadores_tabla=pd.read_sql_query(jugadores_query,NBA)

player1=st.selectbox(
    "Seleccione un jugador",
    list(jugadores_tabla.jugador),
    key="p1"
)

resumen_query=players.query(player1)


resumen_tabla=players.resumen_player(resumen_query,NBA)
st.write(resumen_tabla.style.highlight_max().format("{:.2f}"))

st.markdown("---")

st.markdown("""## Elija un jugador para comparar 
En la siguiente parte puedes seleccionar otro jugador para comparar carreras, en este caso tienes que dar click en el boton 
para poder correr la comparación :two_men_holding_hands:
""")

player2=st.selectbox(
    "Seleccione un jugador",
    list(jugadores_tabla.jugador),
    key="p2"
)


comparar=st.button(
    "Iniciar comparación"
)

if comparar:
    comparacion=players.compara_player(player1,player2,NBA)
    st.write(comparacion)
else:
    st.write("No se han realizado comparaciones")
