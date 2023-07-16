# import mysql.connector as connection
import pandas as pd
import streamlit as st
import pymysql
pymysql.install_as_MySQLdb()


NBA=st.experimental_connection("mysql",type="sql")

temporadas_query="""
select SEASON as temporada
from NBA.games
group by temporada
order by temporada desc
"""

temporadas_tabla=NBA.query(temporadas_query)
# pd.read_sql_query(temporadas_query,NBA)

season=st.selectbox(
    "Seleccione una temporada",
    list(temporadas_tabla.temporada)
)


equipos_query=f"""
with cte as (
select GAME_ID,
TEAM_ID,
TEAM_CITY,
PLAYER_NAME,
PTS
from NBA.games_details)
select a.TEAM_CITY as equipo
from cte as a
left join NBA.games as b
on a.GAME_ID=b.GAME_ID
where b.SEASON={int(season)}
group by equipo
"""

equipos_tabla=NBA.query(equipos_query)
team=st.selectbox(
    "Seleccione un equipo",
    list(equipos_tabla.equipo)
)


resumen_query=f"""
with cte as (
select GAME_ID,
    TEAM_ID,
    TEAM_CITY,
    PLAYER_NAME,
    PTS,
    REB,
    AST,
    STL,
    BLK
from NBA.games_details)
select a.TEAM_CITY as Equipo,
    a.PLAYER_NAME as Jugador,
    a.PTS,
    a.REB,
    a.AST,
    a.STL,
    a.BLK,
    b.SEASON as Temporada
from cte as a
left join NBA.games as b
on a.GAME_ID=b.GAME_ID
where b.SEASON={int(season)} and
a.TEAM_CITY="{team}"
"""

resumen_tabla=NBA.query(resumen_query)
st.write(round(resumen_tabla.groupby(["Equipo","Jugador"]).mean(),2))