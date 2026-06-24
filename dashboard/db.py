import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from database.connection import engine
import pandas as pd
import plotly.express as px

def get_transactions():

    query = """
    SELECT *
    FROM transactions
    """

    return pd.read_sql(
        query,
        engine
    )


def get_pipeline_logs():

    query = """
    SELECT *
    FROM pipeline_logs
    ORDER BY run_id DESC
    """

    return pd.read_sql(
        query,
        engine
    )
def get_fraud_data():

    query = """
    SELECT *
    FROM transactions
    WHERE fraud_flag = TRUE
    """

    return pd.read_sql(
        query,
        engine
    )