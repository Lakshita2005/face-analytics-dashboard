import streamlit as st
import pandas as pd
import os

st.markdown("# Reports Center")

if os.path.exists("data_log.csv"):

    df = pd.read_csv("data_log.csv")

    st.dataframe(
        df,
        use_container_width=True,
        height=400
    )

    col1, col2 = st.columns(2)

    csv = df.to_csv(index=False).encode("utf-8")

    col1.download_button(
        "Download Report",
        csv,
        "face_report.csv",
        "text/csv"
    )

    if col2.button("Clear Data"):
        os.remove("data_log.csv")
        st.success("Data cleared")

else:

    st.info("No reports available")
