from crewai import Agent
import google.generativeai as genai
import os

# Set up Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to call Gemini API
def generate_text(prompt):
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    return response.text if response else ""

# Define the Resume Writer Agent
resume_writer = Agent(
    role="Resume Writer",
    goal="Generate a professional resume based on user details and job description",
    backstory="An AI-powered professional resume builder trained in ATS-friendly resume formatting.",
    verbose=True,
    llm=generate_text  # Using Gemini for text generation
)

# Define the Cover Letter Writer Agent
cover_letter_writer = Agent(
    role="Cover Letter Writer",
    goal="Create a personalized cover letter tailored to a specific job description",
    backstory="An AI-powered assistant specializing in drafting impactful cover letters that highlight key skills.",
    verbose=True,
    llm=generate_text  # Using Gemini for text generation
)

