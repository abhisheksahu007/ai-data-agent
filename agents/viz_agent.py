import plotly.express as px
import os

class VizAgent:

    @staticmethod
    def generate(df, plan):
        os.makedirs("charts", exist_ok=True)
        charts = []

        if "distribution" in plan:
            for col in df.select_dtypes(include="number").columns[:3]:
                fig = px.histogram(df, x=col)
                path = f"charts/{col}.png"
                fig.write_image(path)
                charts.append(path)

        if "correlation" in plan:
            corr = df.corr(numeric_only=True)
            fig = px.imshow(corr, text_auto=True)
            path = "charts/correlation.png"
            fig.write_image(path)
            charts.append(path)

        if "category" in plan and len(df.select_dtypes(exclude="number").columns) > 0:
            cat = df.select_dtypes(exclude="number").columns[0]

            vc = df[cat].value_counts().reset_index()
            vc.columns = [cat, "count"]

            fig = px.bar(vc, x=cat, y="count")

            path = "charts/category.png"
            fig.write_image(path)
            charts.append(path)

        return charts