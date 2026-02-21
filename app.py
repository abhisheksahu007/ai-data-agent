import streamlit as st
import pandas as pd
from agents.data_agent import DataAgent
from agents.stats_agent import StatsAgent
from agents.viz_agent import VizAgent
from agents.insight_agent import InsightAgent
from agents.report_agent import ReportAgent

st.set_page_config(page_title="AI Data Analyst", layout="wide")

st.title("🤖 AI Data Understanding Agent")

uploaded = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded:

    with st.spinner("Loading data..."):
        df = DataAgent.load_data(uploaded)

    st.success("Dataset Loaded")

    if st.checkbox("Preview Data"):
        st.dataframe(df.head())

    metadata = DataAgent.analyze(df)

    col1, col2 = st.columns(2)
    col1.metric("Rows", metadata["rows"])
    col2.metric("Columns", metadata["columns"])

    if st.checkbox("Show Missing Values"):
        st.write(metadata["missing_values"])

    if st.button("Run AI Analysis"):

        with st.spinner("Analyzing data..."):

            stats = StatsAgent.summary(df)
            outliers = StatsAgent.outliers(df)

            plan = []
            if metadata["numeric_cols"]:
                plan.append("distribution")
            if len(metadata["numeric_cols"]) > 1:
                plan.append("correlation")
            if metadata["categorical_cols"]:
                plan.append("category")

            charts = VizAgent.generate(df, plan)

            insights = InsightAgent.generate(metadata, stats, outliers)

            try:
                report = ReportAgent.build(insights)

                with open(report, "rb") as f:
                    st.download_button("📄 Download Report", f, "AI_EDA_Report.pdf")

            except Exception as e:
                st.warning("Report generation skipped due to formatting issue.")

        st.subheader("📊 Insights")
        st.write(insights)

        st.subheader("📈 Charts")
        for fig in charts:
            st.plotly_chart(fig, use_container_width=True)

        with open(report, "rb") as f:
            st.download_button(
                label="📄 Download Report",
                data=f,
                file_name="AI_EDA_Report.pdf",
                mime="application/pdf",
                key="download_report_btn"
            )