with source as (
    select * from {{ source('baseball_raw', 'PLAYERS') }}
),

renamed as (
    select
        player_id,
        full_name,
        position,
        bats,
        throws,
        try_to_date(birth_date) as birth_date,
        try_to_date(debut_date) as debut_date,
        active,
        team_id,
        season
    from source
    qualify row_number() over (
        partition by player_id
        order by season desc
    ) = 1
)

select * from renamed
