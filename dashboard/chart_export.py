from pathlib import Path
import plotly.express as px


def save_plotly_chart(fig, filename):

    Path(
        "reports/charts"
    ).mkdir(
        parents=True,
        exist_ok=True
    )

    fig.write_image(
        f"reports/charts/{filename}"
    )