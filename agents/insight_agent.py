from openai import AzureOpenAI
import streamlit as st

client = AzureOpenAI(
    api_key=st.secrets["AZURE_OPENAI_KEY"],
    api_version="2024-02-15-preview",
    azure_endpoint=st.secrets["AZURE_OPENAI_ENDPOINT"]
)

class InsightAgent:

    @staticmethod
    def generate(metadata, stats, outliers):

        prompt = f"""
        You are a senior business data analyst.

        Dataset Info:
        {metadata}

        Statistics:
        {stats}

        Outliers:
        {outliers}

        Provide:
        - Key Insights
        - Trends
        - Risks
        - Business Recommendations
        """

        response = client.chat.completions.create(
            model=st.secrets["AZURE_OPENAI_DEPLOYMENT"],
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        return response.choices[0].message.content