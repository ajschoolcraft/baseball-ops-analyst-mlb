with games as (
    select * from {{ ref('stg_games') }}
),

season_agg as (
    select
        season as season_year,
        count(*) as game_count
    from games
    group by season
)

select
    season_year,
    game_count
from season_agg
