#!/usr/bin/env python3

import reportlab
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_pie_chart(sorted_data):
    """Generate a pie chart for car sales and save it as an image."""
    car_names = [car[1] for car in sorted_data]  # Ensure it's the formatted name
    sales = [int(car[3]) for car in sorted_data]  # Ensure total sales are integers

    plt.figure(figsize=(6, 6))
    plt.pie(sales, labels=car_names, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title("Total Car Sales Distribution")
    plt.axis("equal")  # Ensures the pie chart is a circle
    pie_chart_path = "/tmp/car_sales_chart.png"
    plt.savefig(pie_chart_path)
    plt.close()

    return pie_chart_path

def generate(filename, title, additional_info, table_data):
    """Generate a PDF report with a title, additional information, a table, and a pie chart."""
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)

    # Title and Additional Info
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(additional_info, styles["BodyText"])

    # Table Formatting
    table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                   ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                   ('ALIGN', (0,0), (-1,-1), 'CENTER')]
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

    # Generate Pie Chart and Include It
    pie_chart_path = generate_pie_chart(table_data[1:])  # Skip table headers
    report_pie_chart = Image(pie_chart_path, width=400, height=300)

    # Add Elements to the Report
    empty_line = Spacer(1, 20)
    report.build([report_title, empty_line, report_info, empty_line, report_table, empty_line, report_pie_chart])
