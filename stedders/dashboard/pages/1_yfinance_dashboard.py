from datetime import date, timedelta
from pathlib import Path
from pprint import pprint
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import yfinance
import polars as pl

dashboard_name = "YFinance Dashboard"

st.set_page_config(
    page_title=dashboard_name,
    page_icon=":money:",
    layout="wide",
    menu_items={"About": "Example dashboard as a kind of portfolio"},
)
st.title(dashboard_name)


st.write("A simple dashboard sourcing data from Yahoo Finance")
nasdaq_stocks = sorted(
    [
        f"{stock['Symbol']} ({stock['Name']})"
        for stock in pl.read_csv(
            Path(__file__).parent.parent / "reference_data/nasdaq.csv"
        )
        .select(pl.struct(pl.col("Symbol"), pl.col("Name")))
        .to_dict(as_series=False)["Symbol"]
    ]
)

selected_tickers = st.multiselect("Select Tickers:", nasdaq_stocks)
date_range_col, other_col = st.columns(2)

start, end = None, None
with date_range_col:
    try:
        start, end = st.date_input(
            "Select date range:",
            value=(date.today() - timedelta(days=30), date.today()),
            max_value=date.today(),
        )
    except ValueError:
        pass


if selected_tickers and start and end:
    fig = go.Figure()
    if len(selected_tickers) == 1:
        ticker_name = [x.split(" ")[0] for x in selected_tickers][0]
        ticker = yfinance.Ticker(ticker_name)
        ticker_history = ticker.history(start=start, end=end)

        fig = fig.add_trace(
            go.Scatter(
                x=ticker_history.index, y=ticker_history["Close"], name=ticker_name
            )
        )
    else:
        tickers = yfinance.Tickers(
            " ".join([x.split(" ")[0] for x in selected_tickers])
        )
        tickers_history = tickers.history(start=start, end=end)
        for ticker in tickers_history["Close"]:
            fig = fig.add_trace(
                go.Scatter(
                    x=tickers_history.index,
                    y=tickers_history["Close"][ticker],
                    name=ticker,
                )
            )
    st.plotly_chart(fig, use_container_width=True)
