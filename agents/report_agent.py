from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import os

class ReportAgent:

    @staticmethod
    def build(insights, charts):

        os.makedirs("output", exist_ok=True)
        path = "output/AI_EDA_Report.pdf"

        doc = SimpleDocTemplate(path, pagesize=A4)
        styles = getSampleStyleSheet()

        story = []
        story.append(Paragraph("AI Data Insights Report", styles['Title']))
        story.append(Spacer(1,20))
        story.append(Paragraph(insights, styles['BodyText']))

        for chart in charts:
            if os.path.exists(chart):
                story.append(Spacer(1,20))
                story.append(Image(chart, width=400, height=250))

        doc.build(story)
        return path