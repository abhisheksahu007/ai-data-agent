from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import os

class ReportAgent:

    @staticmethod
    def build(insights, charts=None):

        os.makedirs("output", exist_ok=True)
        file_path = "output/AI_EDA_Report.pdf"

        doc = SimpleDocTemplate(file_path, pagesize=A4)
        styles = getSampleStyleSheet()

        story = []

        story.append(Paragraph("AI Data Insights Report", styles['Title']))
        story.append(Spacer(1, 20))
        story.append(Paragraph(insights.replace("\n", "<br/>"), styles['BodyText']))

        doc.build(story)

        return file_path