from database.connection import engine
from sqlalchemy import text


def load_data(df):

    with engine.connect() as conn:

        conn.execute(
            text(
                "TRUNCATE TABLE transactions"
            )
        )

        conn.commit()

    print(
        "Old transactions deleted."
    )

    df.to_sql(
        "transactions",
        engine,
        if_exists="append",
        index=False
    )

    print(
        f"{len(df)} records loaded successfully."
    )