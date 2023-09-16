import streamlit as st

dashboard_name = "Luke Stedman's Portfolio Dashboard"
st.set_page_config(
    page_title=dashboard_name,
    page_icon=":beer:",
    layout="wide",
    menu_items={"About": "Example dashboard as a kind of portfolio"},
)

st.title(dashboard_name)

st.header("About")

st.write(
    "Just a couple of small dashboards I whipped up and deployed to AWS to demonstrate my skills."
)

st.subheader("Dashboards")
st.write("Please select a dashboard from the menu on the left")
st.write(
    "<b>yfinance dashboard:</b> A simple dashboard reading data from the YFinance package and plotting it",
    unsafe_allow_html=True,
)
st.write(
    "<b>random walk:</b> Generate random timeseries of data for fake companies",
    unsafe_allow_html=True,
)
