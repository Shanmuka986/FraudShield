from datetime import datetime
import os

from simulator.generate_transactions import (
    generate_transactions
)

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from etl.logger import log_pipeline_run


start_time = datetime.now()

try:

    # ==========================
    # GENERATE RAW DATA
    # ==========================

    os.makedirs(
        "data/raw",
        exist_ok=True
    )

    generated_df = generate_transactions(
        1000
    )

    generated_df.to_csv(
        "data/raw/transactions.csv",
        index=False
    )

    print(
        f"Generated {len(generated_df)} records"
    )

    # ==========================
    # EXTRACT
    # ==========================

    df = extract_data()

    # ==========================
    # TRANSFORM
    # ==========================

    df = transform_data(df)

    # ==========================
    # LOAD
    # ==========================

    load_data(df)

    # ==========================
    # LOG SUCCESS
    # ==========================

    end_time = datetime.now()

    duration = (
        end_time - start_time
    ).total_seconds()

    log_pipeline_run(
        start_time=start_time,
        end_time=end_time,
        rows_generated=len(generated_df),
        rows_loaded=len(df),
        status="SUCCESS",
        duration_seconds=duration
    )

    print(
        "ETL Pipeline Completed Successfully"
    )

except Exception as e:

    end_time = datetime.now()

    duration = (
        end_time - start_time
    ).total_seconds()

    try:

        log_pipeline_run(
            start_time=start_time,
            end_time=end_time,
            rows_generated=0,
            rows_loaded=0,
            status="FAILED",
            duration_seconds=duration
        )

    except Exception:
        pass

    raise e