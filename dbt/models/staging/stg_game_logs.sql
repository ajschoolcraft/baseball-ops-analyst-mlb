with source as (
    select * from {{ source('baseball_raw', 'GAME_LOGS') }}
),

renamed as (
    select
        player_id,
        game_id,
        try_to_date(game_date) as game_date,
        season,
        team_id,
        player_type,
        at_bats,
        hits,
        doubles,
        triples,
        home_runs,
        rbi,
        runs,
        walks,
        strikeouts,
        stolen_bases,
        plate_appearances,
        innings_pitched::float as innings_pitched,
        earned_runs,
        pitching_strikeouts,
        pitching_walks,
        pitching_hits,
        pitching_home_runs,
        pitches
    from source
    qualify row_number() over (
        partition by player_id, game_id, player_type
        order by game_date desc
    ) = 1
)

select * from renamed
