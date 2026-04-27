with season_stats as (
    select * from {{ ref('stg_season_stats') }}
),

statcast_season as (
    select
        batter_id as player_id,
        game_year as season,
        avg(launch_speed) as avg_exit_velocity,
        avg(launch_angle) as avg_launch_angle,
        count(case when launch_speed_angle = 6 then 1 end) as barrel_count,
        count(*) as batted_ball_events,
        round(
            count(case when launch_speed_angle = 6 then 1 end)
            / nullif(count(*), 0) * 100,
            1
        ) as barrel_pct,
        avg(xwoba) as xwoba
    from {{ ref('stg_statcast') }}
    group by batter_id, game_year
)

select
    ss.player_id,
    ss.player_name,
    ss.season,
    ss.team_id,
    ss.player_type,
    ss.games_played,
    ss.plate_appearances,
    ss.at_bats,
    ss.hits,
    ss.doubles,
    ss.triples,
    ss.home_runs,
    ss.rbi,
    ss.walks,
    ss.strikeouts,
    ss.stolen_bases,
    ss.batting_avg,
    ss.on_base_pct,
    ss.slugging_pct,
    ss.ops,
    ss.babip,
    ss.hit_by_pitches,
    ss.games_started,
    ss.wins,
    ss.losses,
    ss.era,
    ss.innings_pitched,
    ss.earned_runs,
    ss.whip,
    ss.strikeouts_per_9,
    ss.walks_per_9,
    ss.saves,
    ss.holds,
    case
        when ss.player_type = 'pitcher' and ss.innings_pitched > 0 then
            round(
                (
                    (13 * ss.home_runs)
                    + (3 * (ss.walks + coalesce(ss.hit_by_pitches, 0)))
                    - (2 * ss.strikeouts)
                ) / ss.innings_pitched + 3.10,
                2
            )
    end as fip,
    sc.avg_exit_velocity,
    sc.avg_launch_angle,
    sc.barrel_count,
    sc.barrel_pct,
    sc.batted_ball_events,
    sc.xwoba
from season_stats ss
left join statcast_season sc
    on ss.player_id = sc.player_id
    and ss.season = sc.season
