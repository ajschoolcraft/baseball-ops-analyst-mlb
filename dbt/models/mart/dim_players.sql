with players as (
    select * from {{ ref('stg_players') }}
)

select
    player_id,
    full_name,
    position,
    bats,
    throws,
    birth_date,
    debut_date,
    active
from players
