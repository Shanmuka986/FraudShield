from datetime import datetime

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from etl.logger import log_pipeline_run


start_time = datetime.now()

try:

    df = extract_data()

    df = transform_data(df)

    load_data(df)

    end_time = datetime.now()

    duration = (
        end_time - start_time
    ).total_seconds()

    log_pipeline_run(
        start_time=start_time,
        end_time=end_time,
        rows_generated=len(df),
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

    log_pipeline_run(
        start_time=start_time,
        end_time=end_time,
        rows_generated=0,
        rows_loaded=0,
        status="FAILED",
        duration_seconds=duration
    )

    raise e