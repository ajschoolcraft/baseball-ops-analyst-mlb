with games as (
    select game_id from {{ ref('stg_games') }}
),

game_logs as (
    select * from {{ ref('stg_game_logs') }}
    where player_type = 'batter'
    and game_id in (select game_id from games)
),

statcast_game as (
    select
        batter_id as player_id,
        game_pk as game_id,
        avg(launch_speed) as avg_exit_velocity,
        avg(launch_angle) as avg_launch_angle,
        count(case when launch_speed_angle = 6 then 1 end) as barrel_count,
        count(*) as batted_ball_events,
        avg(xwoba) as avg_xwoba
    from {{ ref('stg_statcast') }}
    group by batter_id, game_pk
)

select
    gl.player_id,
    gl.game_id,
    gl.game_date,
    gl.season,
    gl.team_id,
    gl.at_bats,
    gl.hits,
    gl.doubles,
    gl.triples,
    gl.home_runs,
    gl.rbi,
    gl.runs,
    gl.walks,
    gl.strikeouts,
    gl.stolen_bases,
    gl.plate_appearances,
    sc.avg_exit_velocity,
    sc.avg_launch_angle,
    sc.barrel_count,
    sc.batted_ball_events,
    sc.avg_xwoba
from game_logs gl
left join statcast_game sc
    on gl.player_id = sc.player_id
    and gl.game_id = sc.game_id
