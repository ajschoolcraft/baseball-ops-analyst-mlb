with source as (
    select * from {{ source('baseball_raw', 'TEAMS') }}
),

renamed as (
    select
        team_id,
        name,
        abbreviation,
        case
            when league ilike '%american%' then 'AL'
            when league ilike '%national%' then 'NL'
            else league
        end as league,
        division
    from source
)

select * from renamed
