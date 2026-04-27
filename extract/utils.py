import os

import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
from snowflake.connector.pandas_tools import write_pandas

load_dotenv()


def get_connection():
    return snowflake.connector.connect(
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        user=os.environ["SNOWFLAKE_USER"],
        password=os.environ["SNOWFLAKE_PASSWORD"],
        database=os.environ.get("SNOWFLAKE_DATABASE", "BASEBALL_ANALYTICS"),
        warehouse=os.environ.get("SNOWFLAKE_WAREHOUSE", "BASEBALL_WH"),
    )


def load_to_snowflake(df, table_name, schema="RAW"):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        database = os.environ.get("SNOWFLAKE_DATABASE", "BASEBALL_ANALYTICS")
        cursor.execute(f"DROP TABLE IF EXISTS {database}.{schema}.{table_name}")
        df.columns = [c.upper() for c in df.columns]
        write_pandas(
            conn,
            df,
            table_name,
            schema=schema,
            database=database,
            auto_create_table=True,
        )
        print(f"Loaded {len(df)} rows to {schema}.{table_name}")
    finally:
        conn.close()
