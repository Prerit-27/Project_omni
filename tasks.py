from crewai import Task
from agents import resume_writer, cover_letter_writer
from tools import extract_job_keywords, format_resume, format_cover_letter

# Task for Resume Writer Agent
resume_task = Task(
    description="Generate a professional ATS-friendly resume based on the provided user details and job description.",
    agent=resume_writer,
    expected_output="A well-structured resume matching the job requirements."
)

# Task for Cover Letter Writer Agent
cover_letter_task = Task(
    description="Generate a tailored cover letter for the given job description, highlighting relevant skills and experience.",
    agent=cover_letter_writer,
    expected_output="A personalized cover letter that aligns with the job posting."
)

