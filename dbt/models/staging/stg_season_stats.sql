with source as (
    select * from {{ source('baseball_raw', 'SEASON_STATS') }}
),

renamed as (
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
        avg::float as batting_avg,
        obp::float as on_base_pct,
        slg::float as slugging_pct,
        ops::float as ops,
        babip::float as babip,
        hit_by_pitches,
        games_started,
        wins,
        losses,
        era::float as era,
        innings_pitched::float as innings_pitched,
        earned_runs,
        whip::float as whip,
        strikeouts_per_9::float as strikeouts_per_9,
        walks_per_9::float as walks_per_9,
        saves,
        holds
    from source
)

select * from renamed
