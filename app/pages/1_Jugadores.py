import pandas as pd
import streamlit as st
import pymysql
pymysql.install_as_MySQLdb()
import funciones.players as players


NBA=st.experimental_connection("mysql",type="sql")


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

jugadores_tabla=NBA.query(jugadores_query)

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
