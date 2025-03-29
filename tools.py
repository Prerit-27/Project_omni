import google.generativeai as genai
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from textwrap import wrap

def extract_job_keywords(job_description):
    """Extracts important keywords from the job description using Gemini."""
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(
        ["Extract key skills and qualifications from this job description:", job_description]
    )
    return response.text.strip()

def format_resume(user_details, job_keywords):
    """Formats the resume with the given user details and job keywords."""
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(
        ["Generate a professional, ATS-friendly resume using the given details:",
         f"User Details: {user_details}\nJob Keywords: {job_keywords}"]
    )
    return response.text.strip()

def format_cover_letter(user_details, job_description):
    """Creates a personalized cover letter based on the job description."""
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(
        ["Generate a compelling, job-specific cover letter:",
         f"User Details: {user_details}\nJob Description: {job_description}"]
    )
    return response.text.strip()

def save_as_pdf(content, filename):
    """Saves text content as a properly formatted PDF file."""
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Set font and margins
    c.setFont("Helvetica", 12)
    left_margin = 50
    top_margin = height - 50
    line_height = 18  # Space between lines
    max_width = width - 2 * left_margin  # Maximum width for text wrapping

    # Split content into lines and wrap them properly
    lines = []
    for line in content.split("\n"):
        wrapped_lines = wrap(line, width=90)  # Adjust word wrapping
        lines.extend(wrapped_lines if wrapped_lines else [" "])  # Preserve blank lines

    y_position = top_margin  # Start position

    for line in lines:
        if y_position < 50:  # If not enough space, add a new page
            c.showPage()
            c.setFont("Helvetica", 12)
            y_position = top_margin

        c.drawString(left_margin, y_position, line)
        y_position -= line_height  # Move down for next line

    c.save()