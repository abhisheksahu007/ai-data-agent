import plotly.express as px

class VizAgent:

    @staticmethod
    def generate(df, plan):
        charts = []

        # numeric distributions
        if "distribution" in plan:
            for col in df.select_dtypes(include="number").columns[:3]:
                fig = px.histogram(df, x=col, title=f"Distribution of {col}")
                charts.append(fig)

        # correlation heatmap
        if "correlation" in plan:
            corr = df.corr(numeric_only=True)
            fig = px.imshow(corr, text_auto=True, title="Correlation Heatmap")
            charts.append(fig)

        # categorical analysis
        cat_cols = df.select_dtypes(exclude="number").columns
        if "category" in plan and len(cat_cols) > 0:
            cat = cat_cols[0]
            vc = df[cat].value_counts().head(10).reset_index()
            vc.columns = [cat, "count"]

            fig = px.bar(vc, x=cat, y="count", title=f"{cat} Distribution")
            charts.append(fig)

        return charts