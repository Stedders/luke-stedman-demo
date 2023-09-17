from datetime import time, date
from datetime import timedelta

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import polars as pl
import streamlit as st
from faker import Faker

dashboard_name = "Random Walk Dashboard"

st.set_page_config(
    page_title=dashboard_name,
    page_icon=":money:",
    layout="wide",
    menu_items={"About": "Example dashboard as a kind of portfolio"},
)
st.title(dashboard_name)

st.write("Generate a random time-series based on a seed for fake companies.")

seed_col, companies_col, date_range_col, generate_col = st.columns(4)

seed, companies, start, end = None, None, None, None

with seed_col:
    seed = st.number_input("Seed to generate from:", value=123456)

with companies_col:
    companies = st.number_input(
        "No. of Companies to generate:", min_value=1, max_value=199
    )

with date_range_col:
    try:
        start, end = st.date_input(
            "Range to generate data for:",
            value=(date.today() - timedelta(days=180), date.today()),
        )
    except ValueError:
        pass

generate = st.button(
    "Generate",
    disabled=seed is None and companies is None and start is None and end is None,
)


def generate_time_series(
    seed_input: ..., companies_input: int, start_input: date, end_input: date
) -> pd.DataFrame:
    # Initialize the randomisation
    fake = Faker()
    fake.seed_instance(seed_input)
    np.random.seed(seed_input)

    # Create a timerange between the start and end dates at a 1 minute interval
    time_series = pl.DataFrame(
        {
            "timestamp": pl.datetime_range(
                start=start_input,
                end=end_input,
                interval="1m",
                eager=True,
            )
        }
        # Filter timestamps so the time range is between 09:30 - 16:30
    ).filter(pl.col("timestamp").cast(pl.Time).is_between(time(9, 30), time(16, 30)))
    time_series = pl.concat(
        (
            # Concat the range defined above
            time_series,
            # Derive from a numpy array
            pl.from_numpy(
                # Concat numpy arrays
                data=np.concatenate(
                    (
                        # Create a random 1D (columns) range based on the number of companoes, init between 0 - 150
                        np.random.random(size=(1, companies_input)) * 150,
                        # Concat a random 2D array based on the length of the time_series range and number of companies
                        (
                            np.random.random(
                                size=(len(time_series) - 1, companies_input)
                            )
                            * 0.1
                            # randoml
                        )
                        * np.random.choice(
                            a=[-1, 0, 1],
                            size=(len(time_series) - 1, companies_input),
                            p=[0.3, 0.3, 0.4],
                        ),
                    ),
                    axis=0,
                ),
                schema=[fake.company() for _ in range(companies_input)],
            ).select(pl.all().cumsum()),
        ),
        how="horizontal",
    )

    return time_series.to_pandas().set_index("timestamp")


if generate:
    time_series_df = generate_time_series(
        seed_input=seed,
        companies_input=companies,
        start_input=start,
        end_input=end,
    )
    fig = go.Figure()
    for company in time_series_df.columns:
        fig = fig.add_trace(
            go.Scatter(
                x=time_series_df.index,
                y=time_series_df[company],
                name=company,
            )
        )
    st.plotly_chart(fig, use_container_width=True)
