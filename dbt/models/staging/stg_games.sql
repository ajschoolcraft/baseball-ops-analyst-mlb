with source as (
    select * from {{ source('baseball_raw', 'GAMES') }}
),

renamed as (
    select
        game_id,
        try_to_date(game_date) as game_date,
        game_type,
        home_team_id,
        away_team_id,
        home_score,
        away_score,
        venue_name,
        status,
        season
    from source
    qualify row_number() over (
        partition by game_id
        order by game_date desc
    ) = 1
)

select * from renamed
