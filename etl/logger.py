from database.connection import engine
from sqlalchemy import text


def log_pipeline_run(
    start_time,
    end_time,
    rows_generated,
    rows_loaded,
    status,
    duration_seconds
):

    query = text("""
        INSERT INTO pipeline_logs
        (
            start_time,
            end_time,
            rows_generated,
            rows_loaded,
            status,
            duration_seconds
        )
        VALUES
        (
            :start_time,
            :end_time,
            :rows_generated,
            :rows_loaded,
            :status,
            :duration_seconds
        )
    """)

    with engine.begin() as conn:

        conn.execute(
            query,
            {
                "start_time": start_time,
                "end_time": end_time,
                "rows_generated": rows_generated,
                "rows_loaded": rows_loaded,
                "status": status,
                "duration_seconds": duration_seconds
            }
        )