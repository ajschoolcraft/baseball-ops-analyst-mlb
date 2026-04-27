with source as (
    select * from {{ source('baseball_raw', 'STATCAST') }}
),

renamed as (
    select
        game_pk,
        try_to_date(game_date) as game_date,
        game_year,
        batter as batter_id,
        pitcher as pitcher_id,
        player_name,
        events,
        description,
        bb_type,
        stand,
        p_throws,
        home_team,
        away_team,
        pitch_type,
        pitch_name,
        release_speed,
        release_spin_rate,
        effective_speed,
        launch_speed,
        launch_angle,
        launch_speed_angle,
        hit_distance_sc as hit_distance,
        estimated_woba_using_speedangle as xwoba,
        estimated_ba_using_speedangle as xba,
        woba_value,
        woba_denom,
        bat_speed,
        swing_length
    from source
    where launch_speed is not null
)

select * from renamed
