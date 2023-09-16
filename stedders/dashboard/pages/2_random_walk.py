#
# df = None
# with st.sidebar as sb:
#     st.header("Configuration")
#     company_count = st.slider("No. Companies", min_value=0, max_value=200, value=5)
#     start = st.date_input("Start Date", value=date.today() - timedelta(days=2))
#     end = st.date_input("End Date", value=date.today())
#     open = st.time_input("Open Time", value=time(hour=9))
#     close = st.time_input("Close Time", value=time(hour=16, minute=30))
#     interval_minutes = st.number_input(
#         "Interval (mins)", value=2, min_value=1, max_value=20
#     )
#     # algorithm = st.radio("Algorithm", algorithms)
#
#     # if st.button("Generate Data"):
#     #     df = algorithms[algorithm](
#     #         company_count=company_count,
#     #         interval=timedelta(minutes=interval_minutes),
#     #         timeseries_start=start,
#     #         timeseries_end=end,
#     #         open_time=open,
#     #         close_time=close,
#     #     ).set_index("timestamp")
#
# df: pd.DataFrame | None
# if df is not None:
#     st.plotly_chart(
#         px.line(
#             data_frame=df,
#             x=df.index,
#             y=df.columns,
#         ),
#         use_container_width=True,
#     )
#
#     base_filename = f"{datetime.now().isoformat().replace(':','')}_random_walk"
#     st.download_button(
#         "Download as CSV",
#         df.to_csv().encode("utf-8"),
#         f"{base_filename}.csv",
#         "text/csv",
#     )
#     output = io.BytesIO()
#     writer = pd.ExcelWriter(output)
#     df.to_excel(
#         writer,
#         sheet_name="Random Walk",
#     )
#     writer.close()
#     st.download_button(
#         "Download as Excel", data=output, file_name=f"{base_filename}.xlsx"
#     )
