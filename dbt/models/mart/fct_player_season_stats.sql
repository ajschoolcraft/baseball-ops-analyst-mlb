with batter_season as (
    select
        gl.player_id,
        gl.player_name,
        gl.season,
        gl.team_id,
        'batter' as player_type,
        count(distinct gl.game_id) as games_played,
        sum(gl.plate_appearances) as plate_appearances,
        sum(gl.at_bats) as at_bats,
        sum(gl.hits) as hits,
        sum(gl.doubles) as doubles,
        sum(gl.triples) as triples,
        sum(gl.home_runs) as home_runs,
        sum(gl.rbi) as rbi,
        sum(gl.walks) as walks,
        sum(gl.strikeouts) as strikeouts,
        sum(gl.stolen_bases) as stolen_bases,
        round(sum(gl.hits) / nullif(sum(gl.at_bats), 0), 3) as batting_avg,
        round(
            (sum(gl.hits) + sum(gl.walks))
            / nullif(sum(gl.plate_appearances), 0),
            3
        ) as on_base_pct,
        round(
            (sum(gl.hits) + sum(gl.doubles) + 2 * sum(gl.triples) + 3 * sum(gl.home_runs))
            / nullif(sum(gl.at_bats), 0),
            3
        ) as slugging_pct,
        round(
            (sum(gl.hits) + sum(gl.walks))
            / nullif(sum(gl.plate_appearances), 0)
            + (sum(gl.hits) + sum(gl.doubles) + 2 * sum(gl.triples) + 3 * sum(gl.home_runs))
            / nullif(sum(gl.at_bats), 0),
            3
        ) as ops,
        round(
            (sum(gl.hits) - sum(gl.home_runs))
            / nullif(sum(gl.at_bats) - sum(gl.strikeouts) - sum(gl.home_runs), 0),
            3
        ) as babip,
        null::int as hit_by_pitches,
        null::int as games_started,
        null::int as wins,
        null::int as losses,
        null::float as era,
        null::float as innings_pitched,
        null::int as earned_runs,
        null::float as whip,
        null::float as strikeouts_per_9,
        null::float as walks_per_9,
        null::int as saves,
        null::int as holds
    from {{ ref('stg_game_logs') }} gl
    where gl.player_type = 'batter'
    group by gl.player_id, gl.player_name, gl.season, gl.team_id
),

pitcher_season as (
    select
        player_id,
        player_name,
        season,
        team_id,
        player_type,
        games_played,
        plate_appearances,
        at_bats,
        hits,
        doubles,
        triples,
        home_runs,
        rbi,
        walks,
        strikeouts,
        stolen_bases,
        batting_avg,
        on_base_pct,
        slugging_pct,
        ops,
        babip,
        hit_by_pitches,
        games_started,
        wins,
        losses,
        era,
        innings_pitched,
        earned_runs,
        whip,
        strikeouts_per_9,
        walks_per_9,
        saves,
        holds
    from {{ ref('stg_season_stats') }}
    where player_type = 'pitcher'
),

all_seasons as (
    select * from batter_season
    union all
    select * from pitcher_season
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
    s.player_id,
    s.player_name,
    s.season,
    s.team_id,
    s.player_type,
    s.games_played,
    s.plate_appearances,
    s.at_bats,
    s.hits,
    s.doubles,
    s.triples,
    s.home_runs,
    s.rbi,
    s.walks,
    s.strikeouts,
    s.stolen_bases,
    s.batting_avg,
    s.on_base_pct,
    s.slugging_pct,
    s.ops,
    s.babip,
    s.hit_by_pitches,
    s.games_started,
    s.wins,
    s.losses,
    s.era,
    s.innings_pitched,
    s.earned_runs,
    s.whip,
    s.strikeouts_per_9,
    s.walks_per_9,
    s.saves,
    s.holds,
    case
        when s.player_type = 'pitcher' and s.innings_pitched > 0 then
            round(
                (
                    (13 * s.home_runs)
                    + (3 * (s.walks + coalesce(s.hit_by_pitches, 0)))
                    - (2 * s.strikeouts)
                ) / s.innings_pitched + 3.10,
                2
            )
    end as fip,
    sc.avg_exit_velocity,
    sc.avg_launch_angle,
    sc.barrel_count,
    sc.barrel_pct,
    sc.batted_ball_events,
    sc.xwoba
from all_seasons s
left join statcast_season sc
    on s.player_id = sc.player_id
    and s.season = sc.season
