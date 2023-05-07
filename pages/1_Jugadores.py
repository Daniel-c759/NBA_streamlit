import mysql.connector as connection
import pandas as pd
import streamlit as st
import funciones.players as players

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

resumen_query=f"""
with cte as (
select GAME_ID,
    TEAM_ID,
    TEAM_CITY,
    PLAYER_NAME,
    MIN,
    FG_PCT,
    FG3_PCT,
    FT_PCT,
    PTS,
    REB,
    AST,
    STL,
    BLK,
    PLUS_MINUS
from NBA.games_details)
select a.TEAM_CITY as Equipo,
    a.PLAYER_NAME as Jugador,
    a.MIN as minutos,
    a.FG_PCT,
    a.FG3_PCT,
    a.FT_PCT,
    a.PTS,
    a.REB,
    a.AST,
    a.STL,
    a.BLK,
    b.SEASON as Temporada
from cte as a
left join NBA.games as b
on a.GAME_ID=b.GAME_ID
where a.PLAYER_NAME="{player1}"
"""

resumen_tabla=players.resumen_player(resumen_query,NBA)
st.write(resumen_tabla)

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
