import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.markdown("# Analytics Dashboard")
st.markdown("Visual insights from face detection data")

if os.path.exists("data_log.csv"):

    df = pd.read_csv("data_log.csv")

    col1, col2, col3 = st.columns(3)

    col1.metric("Max Faces", df["Face Count"].max())
    col2.metric("Average Faces", int(df["Face Count"].mean()))
    col3.metric("Total Records", len(df))

    st.divider()

    fig = px.area(
        df,
        x="Time",
        y="Face Count",
        title="Face Detection Trend",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)

else:

    st.warning("No analytics data available")
