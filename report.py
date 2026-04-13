from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(result, score, ph, tds, turbidity):
    doc = SimpleDocTemplate("report.pdf")
    styles = getSampleStyleSheet()

    content = []
    content.append(Paragraph("Water Quality Report", styles['Title']))
    content.append(Spacer(1, 10))

    content.append(Paragraph(f"Result: {result}", styles['Normal']))
    content.append(Paragraph(f"Score: {score:.1f}", styles['Normal']))
    content.append(Paragraph(f"pH: {ph}", styles['Normal']))
    content.append(Paragraph(f"TDS: {tds}", styles['Normal']))
    content.append(Paragraph(f"Turbidity: {turbidity}", styles['Normal']))

    doc.build(content)