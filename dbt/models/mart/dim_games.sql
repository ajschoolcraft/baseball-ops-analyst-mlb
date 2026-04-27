with games as (
    select * from {{ ref('stg_games') }}
)

select
    game_id,
    game_date,
    home_team_id,
    away_team_id,
    venue_name,
    home_score,
    away_score,
    season
from games
