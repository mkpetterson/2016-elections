#!/usr/bin/env python3
"""
Generate PDF report for student project evaluation using reportlab
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime
import os

# Create PDF
output_path = '/home/user/2016-elections/PROJECT_EVALUATION_REPORT.pdf'
doc = SimpleDocTemplate(output_path, pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)

# Container for the 'Flowable' objects
elements = []

# Define styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='CustomTitle',
                          parent=styles['Heading1'],
                          fontSize=24,
                          textColor=colors.HexColor('#1f4e79'),
                          spaceAfter=30,
                          alignment=TA_CENTER))

styles.add(ParagraphStyle(name='CustomHeading1',
                          parent=styles['Heading1'],
                          fontSize=16,
                          textColor=colors.HexColor('#1f4e79'),
                          spaceAfter=12))

styles.add(ParagraphStyle(name='CustomHeading2',
                          parent=styles['Heading2'],
                          fontSize=13,
                          spaceAfter=10))

styles.add(ParagraphStyle(name='CustomHeading3',
                          parent=styles['Heading3'],
                          fontSize=11,
                          spaceAfter=6))

styles.add(ParagraphStyle(name='Justify',
                          parent=styles['BodyText'],
                          alignment=TA_JUSTIFY,
                          fontSize=10,
                          leading=14))

styles.add(ParagraphStyle(name='CustomBullet',
                          parent=styles['BodyText'],
                          fontSize=10,
                          leftIndent=20,
                          leading=14))

# Title Page
elements.append(Spacer(1, 1.5*inch))
elements.append(Paragraph("DATA SCIENCE PROJECT EVALUATION", styles['CustomTitle']))
elements.append(Spacer(1, 0.5*inch))
elements.append(Paragraph("Student: Maureen Petterson", styles['Normal']))
elements.append(Paragraph("Project: Predicting the 2016 Presidential Election Using County-Level Demographics", styles['Normal']))
elements.append(Spacer(1, 0.3*inch))
elements.append(Paragraph(f"Evaluation Date: {datetime.now().strftime('%B %d, %Y')}", styles['Normal']))
elements.append(Paragraph("Assignment: End-to-end Data Science Workflow", styles['Normal']))
elements.append(Paragraph("Student Level: Beginner (9-month Data Science Program)", styles['Normal']))
elements.append(PageBreak())

# Executive Summary
elements.append(Paragraph("EXECUTIVE SUMMARY", styles['CustomHeading1']))
elements.append(Paragraph(
    "This is an exceptionally strong project for a beginner data science student. The work demonstrates "
    "a complete understanding of the full data science workflow, from data cleaning through modeling to "
    "interpretation. The student shows impressive code organization with modular helper functions, employs "
    "multiple modeling approaches (Linear Regression, Random Forest, Gradient Boosting) with proper validation "
    "techniques, and creates excellent visualizations including choropleth maps. The comprehensive README is "
    "publication-quality.",
    styles['Justify']))
elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph(
    "Minor deductions for: (1) a code error in one notebook, (2) limited in-notebook narrative documentation, "
    "and (3) missing dependency management files (requirements.txt) and installation instructions, which "
    "impacts reproducibility.",
    styles['Justify']))
elements.append(Spacer(1, 0.2*inch))

# Grade Box
grade_data = [['RECOMMENDED GRADE: A- (91/100)']]
grade_table = Table(grade_data, colWidths=[6*inch])
grade_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#dcf0dc')),
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 14),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ('TOPPADDING', (0, 0), (-1, -1), 12),
    ('BOX', (0, 0), (-1, -1), 2, colors.black)
]))
elements.append(grade_table)
elements.append(PageBreak())

# Detailed Scoring
elements.append(Paragraph("DETAILED SCORING", styles['CustomHeading1']))
elements.append(Spacer(1, 0.1*inch))

# Technical Data Science Skills
elements.append(Paragraph("Technical Data Science Skills (38/40 pts)", styles['CustomHeading2']))
elements.append(Paragraph("1. Problem Understanding & Approach (8/8 pts)", styles['CustomHeading3']))
elements.append(Paragraph("✓ Excellent problem framing: predicting county-level voting percentages", styles['CustomBullet']))
elements.append(Paragraph("✓ Clear understanding that regression is appropriate for continuous outcomes", styles['CustomBullet']))
elements.append(Paragraph("✓ Thoughtful justification for using demographics only", styles['CustomBullet']))
elements.append(Paragraph("✓ Appropriate train/test split methodology", styles['CustomBullet']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph("2. Data Exploration & Understanding (8/8 pts)", styles['CustomHeading3']))
elements.append(Paragraph("✓ Comprehensive EDA with correlation heatmaps", styles['CustomBullet']))
elements.append(Paragraph("✓ Scatter matrices to identify multicollinearity", styles['CustomBullet']))
elements.append(Paragraph("✓ Histogram comparisons between Trump/Clinton counties", styles['CustomBullet']))
elements.append(Paragraph("✓ Choropleth maps for geographic patterns", styles['CustomBullet']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph("3. Data Preprocessing & Feature Engineering (7/8 pts)", styles['CustomHeading3']))
elements.append(Paragraph("✓ Proper handling of missing data (3 counties dropped, justified)", styles['CustomBullet']))
elements.append(Paragraph("✓ Created meaningful features (vote percentages, turnout rates)", styles['CustomBullet']))
elements.append(Paragraph("✓ One-hot encoding for categorical variables", styles['CustomBullet']))
elements.append(Paragraph("✓ Removed highly correlated features to address multicollinearity", styles['CustomBullet']))
elements.append(Paragraph("⚠ Normalization vs standardization mentioned but not explored in notebooks", styles['CustomBullet']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph("4. Model Development & Validation (8/8 pts)", styles['CustomHeading3']))
elements.append(Paragraph("✓ Three models: Linear Regression, Random Forest, Gradient Boosting", styles['CustomBullet']))
elements.append(Paragraph("✓ Proper 75/25 train/test split", styles['CustomBullet']))
elements.append(Paragraph("✓ KFold cross-validation (5 folds) implemented correctly", styles['CustomBullet']))
elements.append(Paragraph("✓ Feature reduction iterations tested", styles['CustomBullet']))
elements.append(Paragraph("✓ Statistical significance testing with statsmodels", styles['CustomBullet']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph("5. Results Interpretation (7/8 pts)", styles['CustomHeading3']))
elements.append(Paragraph("✓ Clear interpretation of model performance (R² = 0.95-0.96)", styles['CustomBullet']))
elements.append(Paragraph("✓ Analysis of feature importance and coefficients", styles['CustomBullet']))
elements.append(Paragraph("✓ County-level accuracy (96-97% correct predictions)", styles['CustomBullet']))
elements.append(Paragraph("✓ Thoughtful discussion of limitations", styles['CustomBullet']))
elements.append(Paragraph("⚠ No residual analysis or assumption checking for linear regression", styles['CustomBullet']))
elements.append(Spacer(1, 0.2*inch))

# Code Quality
elements.append(Paragraph("Code Quality (20/25 pts)", styles['CustomHeading2']))
elements.append(Paragraph("1. Code Organization & Structure (7/8 pts)", styles['CustomHeading3']))
elements.append(Paragraph("✓ Excellent: Modular code with separate files (cleaners.py, modelers.py, etc.)", styles['CustomBullet']))
elements.append(Paragraph("✓ Logical workflow across multiple notebooks", styles['CustomBullet']))
elements.append(Paragraph("✓ Reusable functions properly organized", styles['CustomBullet']))
elements.append(Paragraph("⚠ Some redundancy between notebooks", styles['CustomBullet']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph("2. Readability & Style (4/6 pts)", styles['CustomHeading3']))
elements.append(Paragraph("✓ Clean, readable code with good variable names", styles['CustomBullet']))
elements.append(Paragraph("✓ Consistent style throughout", styles['CustomBullet']))
elements.append(Paragraph("⚠ Limited code comments within notebooks", styles['CustomBullet']))
elements.append(Paragraph("⚠ Some cells could be better organized (data, data2, data3)", styles['CustomBullet']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph("3. Technical Correctness (4/6 pts)", styles['CustomHeading3']))
elements.append(Paragraph("✓ Most code runs correctly", styles['CustomBullet']))
elements.append(Paragraph("✓ Proper use of sklearn, pandas, numpy, plotly", styles['CustomBullet']))
elements.append(Paragraph("✗ NameError in Linear_regression.ipynb cell 13: data4.columns should be data3.columns", styles['CustomBullet']))
elements.append(Paragraph("⚠ SettingWithCopyWarning in choropleth.ipynb", styles['CustomBullet']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph("4. Library & Tool Usage (5/5 pts)", styles['CustomHeading3']))
elements.append(Paragraph("✓ Appropriate use of pandas, sklearn, statsmodels", styles['CustomBullet']))
elements.append(Paragraph("✓ Plotly for interactive choropleth maps", styles['CustomBullet']))
elements.append(Paragraph("✓ Matplotlib/seaborn for static visualizations", styles['CustomBullet']))
elements.append(PageBreak())

# Documentation & Communication
elements.append(Paragraph("Documentation & Communication (17/20 pts)", styles['CustomHeading2']))
elements.append(Paragraph("1. Notebook Narrative & Explanations (5/8 pts)", styles['CustomHeading3']))
elements.append(Paragraph("✓ Markdown cells present with section headers", styles['CustomBullet']))
elements.append(Paragraph("⚠ Limited narrative: README is excellent but notebooks lack detailed explanations", styles['CustomBullet']))
elements.append(Paragraph("⚠ Missing interpretations directly in notebooks", styles['CustomBullet']))
elements.append(Paragraph("⚠ No discussion of why features were dropped", styles['CustomBullet']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph("2. Visualizations (6/6 pts)", styles['CustomHeading3']))
elements.append(Paragraph("✓ Excellent variety: heatmaps, histograms, scatter matrices, choropleth maps", styles['CustomBullet']))
elements.append(Paragraph("✓ Clear labels and titles on all plots", styles['CustomBullet']))
elements.append(Paragraph("✓ Appropriate color schemes", styles['CustomBullet']))
elements.append(Paragraph("✓ Interactive choropleth maps add significant value", styles['CustomBullet']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph("3. Key Findings & Conclusions (6/6 pts)", styles['CustomHeading3']))
elements.append(Paragraph("✓ Outstanding README: clear, comprehensive, publication-quality", styles['CustomBullet']))
elements.append(Paragraph("✓ Well-articulated conclusions about model performance", styles['CustomBullet']))
elements.append(Paragraph("✓ Thoughtful discussion of most important predictors", styles['CustomBullet']))
elements.append(Paragraph("✓ Honest assessment of limitations and future improvements", styles['CustomBullet']))
elements.append(Spacer(1, 0.2*inch))

# Reproducibility
elements.append(Paragraph("Reproducibility & Best Practices (11/15 pts)", styles['CustomHeading2']))
elements.append(Paragraph("1. Project Organization (5/5 pts)", styles['CustomHeading3']))
elements.append(Paragraph("✓ Clear directory structure (notebooks/, data/, src/, images/)", styles['CustomBullet']))
elements.append(Paragraph("✓ Separated code from data", styles['CustomBullet']))
elements.append(Paragraph("✓ Modular helper functions in src/", styles['CustomBullet']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph("2. Reproducibility (3/5 pts)", styles['CustomHeading3']))
elements.append(Paragraph("✓ All data files included", styles['CustomBullet']))
elements.append(Paragraph("✓ Saved predictions for further analysis", styles['CustomBullet']))
elements.append(Paragraph("✗ NO requirements.txt or environment.yml file", styles['CustomBullet']))
elements.append(Paragraph("✗ NO installation instructions in README", styles['CustomBullet']))
elements.append(Paragraph("⚠ Hard-coded relative paths (../) throughout notebooks", styles['CustomBullet']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph("3. README & Documentation (5/5 pts)", styles['CustomHeading3']))
elements.append(Paragraph("✓ Exceptional README with table of contents", styles['CustomBullet']))
elements.append(Paragraph("✓ Detailed methodology section", styles['CustomBullet']))
elements.append(Paragraph("✓ Visualizations embedded and citations included", styles['CustomBullet']))
elements.append(PageBreak())

# Strengths
elements.append(Paragraph("STRENGTHS", styles['CustomHeading1']))
elements.append(Paragraph(
    "<b>1. OUTSTANDING PROJECT ORGANIZATION:</b> The modular code structure with separate helper modules "
    "(cleaners, explorers, modelers, manipulators) demonstrates professional-level software engineering "
    "practices rarely seen in beginner projects.",
    styles['Justify']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph(
    "<b>2. COMPREHENSIVE DATA SCIENCE WORKFLOW:</b> Complete pipeline from data cleaning → EDA → feature "
    "engineering → multiple models → validation → results interpretation. Shows true understanding of "
    "the entire DS process.",
    styles['Justify']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph(
    "<b>3. EXCELLENT VISUALIZATIONS:</b> The choropleth maps are particularly impressive, showing geographic "
    "voting patterns. The correlation heatmaps, scatter matrices, and comparative histograms all "
    "effectively support the analysis.",
    styles['Justify']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph(
    "<b>4. THOUGHTFUL STATISTICAL ANALYSIS:</b> Used statsmodels to extract p-values and coefficients, showing "
    "understanding beyond just sklearn. The iterative feature reduction based on correlation analysis "
    "demonstrates statistical thinking.",
    styles['Justify']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph(
    "<b>5. PUBLICATION-QUALITY README:</b> The README is exceptionally well-written with clear explanations, "
    "embedded visualizations, proper citations, and thoughtful discussion of results and limitations. "
    "This alone sets the project apart.",
    styles['Justify']))
elements.append(Spacer(1, 0.3*inch))

# Areas for Improvement
elements.append(Paragraph("AREAS FOR IMPROVEMENT", styles['CustomHeading1']))
elements.append(Paragraph(
    "<b>1. FIX RUNTIME ERROR:</b> In Linear_regression.ipynb cell 13, change 'index=data4.columns' to "
    "'index=data3.columns'. This prevents the notebook from running end-to-end without error. Testing "
    "notebooks before submission is critical.",
    styles['Justify']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph(
    "<b>2. ADD DEPENDENCY MANAGEMENT:</b> Create a requirements.txt file with all necessary libraries and versions. "
    "Add installation instructions to the README. This is essential for reproducibility - others cannot "
    "reliably run your code without knowing exact dependencies.",
    styles['Justify']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph(
    "<b>3. ADD MORE NARRATIVE IN NOTEBOOKS:</b> While your README is excellent, the notebooks themselves need "
    "more markdown cells explaining why you chose specific features to drop, interpretation of "
    "visualizations, discussion of model results, and your thought process at each decision point.",
    styles['Justify']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph(
    "<b>4. VALIDATE LINEAR REGRESSION ASSUMPTIONS:</b> For linear regression, check residual plots to verify "
    "homoscedasticity, Q-Q plots to check normality of residuals, and discuss whether assumptions are met.",
    styles['Justify']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph(
    "<b>5. REDUCE NOTEBOOK REDUNDANCY:</b> The RandomForestRegressor.ipynb notebook largely duplicates work from "
    "Linear_regression.ipynb. Consider consolidating or clearly differentiating their purposes.",
    styles['Justify']))
elements.append(PageBreak())

# Red Flags
elements.append(Paragraph("RED FLAGS", styles['CustomHeading1']))
elements.append(Paragraph("<b>NONE</b> - No critical issues found.", styles['Justify']))
elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph("Minor issues noted:", styles['Justify']))
elements.append(Paragraph("✓ Code mostly runs (except one NameError - easily fixable)", styles['CustomBullet']))
elements.append(Paragraph("✓ Statistical methodology is sound", styles['CustomBullet']))
elements.append(Paragraph("✓ No plagiarism indicators (original analysis and code)", styles['CustomBullet']))
elements.append(Paragraph("✓ Results match claims", styles['CustomBullet']))
elements.append(Paragraph("✓ All requirements met", styles['CustomBullet']))
elements.append(Paragraph("⚠ Reproducibility impacted by missing requirements.txt", styles['CustomBullet']))
elements.append(Spacer(1, 0.3*inch))

# Student-Facing Feedback
elements.append(Paragraph("STUDENT-FACING FEEDBACK", styles['CustomHeading1']))
elements.append(Paragraph(
    "Excellent work on this project! Your end-to-end workflow demonstrates a strong grasp of the data "
    "science process, from thoughtful data cleaning through multiple modeling approaches to insightful "
    "interpretation. The modular code organization and professional README are particularly impressive. "
    "Your use of choropleth maps and comprehensive EDA shows creativity and technical skill.",
    styles['Justify']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph(
    "To improve: (1) fix the NameError in the Linear_regression notebook (cell 13), (2) add a requirements.txt "
    "file and installation instructions for reproducibility, (3) add more explanatory markdown cells within "
    "your notebooks to document your thinking, and (4) consider checking linear regression assumptions with "
    "residual plots.",
    styles['Justify']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph(
    "Overall, this is graduate-level work for a beginner student!",
    styles['Justify']))
elements.append(PageBreak())

# Final Grade Summary
elements.append(Paragraph("FINAL GRADE SUMMARY", styles['CustomHeading1']))
elements.append(Spacer(1, 0.2*inch))

score_data = [
    ['Category', 'Points'],
    ['Technical Data Science Skills', '38/40'],
    ['Code Quality', '20/25'],
    ['Documentation & Communication', '17/20'],
    ['Reproducibility & Best Practices', '11/15'],
    ['SUBTOTAL', '86/100']
]
score_table = Table(score_data, colWidths=[4*inch, 1.5*inch])
score_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4e79')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('ALIGN', (1, 0), (1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 11),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('TOPPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 4), (-1, 4), colors.HexColor('#c8dcf0')),
    ('FONTNAME', (0, 4), (-1, 4), 'Helvetica-Bold'),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('ROWBACKGROUNDS', (0, 1), (-1, 3), [colors.white, colors.HexColor('#f0f0f0')])
]))
elements.append(score_table)
elements.append(Spacer(1, 0.2*inch))

elements.append(Paragraph(
    "<b>BONUS POINTS (+5):</b> Awarded for exceptional README quality, professional code organization beyond "
    "requirements, and advanced interactive visualizations.",
    styles['Justify']))
elements.append(Spacer(1, 0.3*inch))

final_grade_data = [['FINAL GRADE: A- (91/100)']]
final_grade_table = Table(final_grade_data, colWidths=[6*inch])
final_grade_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#dcf0dc')),
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 14),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ('TOPPADDING', (0, 0), (-1, -1), 12),
    ('BOX', (0, 0), (-1, -1), 2, colors.black)
]))
elements.append(final_grade_table)
elements.append(Spacer(1, 0.3*inch))

# Additional Notes
elements.append(Paragraph("ADDITIONAL NOTES", styles['CustomHeading2']))
elements.append(Paragraph(
    "This student clearly has strong potential in data science. The project demonstrates systems thinking, "
    "statistical sophistication, communication skills, and technical versatility.",
    styles['Justify']))
elements.append(Spacer(1, 0.1*inch))

elements.append(Paragraph("<b>Recommendation:</b>", styles['Justify']))
elements.append(Paragraph(
    "This student is ready for more advanced coursework and would benefit from projects involving more "
    "complex feature engineering, hyperparameter tuning, time series forecasting, or deep learning "
    "applications. The main growth area is in documenting the analytical thought process directly in "
    "notebooks and ensuring reproducibility through proper dependency management.",
    styles['Justify']))

# Build PDF
doc.build(elements)
print(f"✓ PDF report generated successfully!")
print(f"✓ Location: {output_path}")
print(f"✓ File size: {round(os.path.getsize(output_path) / 1024, 1)} KB")
