from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import os
import re

class ReportAgent:

    @staticmethod
    def clean_text(text):
        # remove unsupported characters
        text = re.sub(r'[^\x00-\x7F]+', ' ', text)
        text = text.replace("\n", "<br/>")
        return text

    @staticmethod
    def build(insights):

        os.makedirs("output", exist_ok=True)
        file_path = "output/AI_EDA_Report.pdf"

        styles = getSampleStyleSheet()
        story = []

        story.append(Paragraph("AI Data Insights Report", styles['Title']))
        story.append(Spacer(1, 20))

        safe_text = ReportAgent.clean_text(insights)

        story.append(Paragraph(safe_text, styles['BodyText']))

        doc = SimpleDocTemplate(file_path, pagesize=A4)
        doc.build(story)

        return file_path