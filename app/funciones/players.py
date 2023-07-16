import pandas as pd

def resumen_player(query, conexion):
    tabla=conexion.query(query)
    tabla[["min","segundos"]]=tabla.minutos.str.split(":",expand=True)
    tabla["min"]=tabla["min"].astype("float")
    tabla["segundos"]=tabla["segundos"].astype("float")
    tabla["segundos"]=tabla["segundos"]/60
    tabla["minutos"]=tabla["min"]+tabla["segundos"]
    variables=["minutos","FG_PCT","FG3_PCT","FT_PCT","PTS","REB","AST","STL","BLK","mas_menos"]
    #devolver información resumida
    resumen=tabla.groupby(["Temporada","Equipo","Jugador"])[variables].mean()
    resumen.sort_index(ascending=False,inplace=True)
    #Regresar tabla
    return round(resumen,2)

def query(player):
    q=f"""
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
        a.PLUS_MINUS as mas_menos,
        b.SEASON as Temporada
    from cte as a
    left join NBA.games as b
    on a.GAME_ID=b.GAME_ID
    where a.PLAYER_NAME="{player}"
    """
    return q

def compara_player(p1,p2,conexion):
    resumen_queryp1=query(p1)
    tabla_p1=resumen_player(resumen_queryp1,conexion)

    resumen_queryp2=query(p2)
    tabla_p2=resumen_player(resumen_queryp2,conexion)
    #Resetear index y tomar columnas pertinentes
    tabla_p1.reset_index(inplace=True)
    tabla_p1=tabla_p1.iloc[:,2:]
    tabla_p2.reset_index(inplace=True)
    tabla_p2=tabla_p2.iloc[:,2:]

    ag1=tabla_p1.groupby("Jugador").mean()
    ag2=tabla_p2.groupby("Jugador").mean()

    total=pd.concat([ag1,ag2],axis=0)
    return total.style.highlight_max().format("{:.2f}")


