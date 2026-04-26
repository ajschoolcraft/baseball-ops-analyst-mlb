with teams as (
    select * from {{ ref('stg_teams') }}
)

select
    team_id,
    name,
    abbreviation,
    league,
    division
from teams
