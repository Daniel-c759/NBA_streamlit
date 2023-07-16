select distinct PLAYER_NAME as jugador
from NBA.games_details
order by jugador desc;

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
where a.PLAYER_NAME={player1};

select SEASON as temporada
from NBA.games
group by temporada
order by temporada desc;

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
where b.SEASON={season}
group by equipo;

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
a.TEAM_CITY={team};