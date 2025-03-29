import streamlit as st
from tasks import resume_task, cover_letter_task
from tools import extract_job_keywords, format_resume, format_cover_letter, save_as_pdf
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("🚨 ERROR: GEMINI_API_KEY is missing! Please check your .env file.")
    st.stop()

genai.configure(api_key=api_key)

# Streamlit UI
st.set_page_config(page_title="Resume & Cover Letter Generator", layout="centered")

st.title("📄 Resume & Cover Letter Generator")
st.markdown("Generate a professional **resume and cover letter** using AI!")

# User Input Form
with st.form(key="user_form"):
    name = st.text_input("Full Name", placeholder="John Doe")
    email = st.text_input("Email", placeholder="john@example.com")
    phone = st.text_input("Phone", placeholder="+1234567890")
    linkedin = st.text_input("LinkedIn URL", placeholder="https://linkedin.com/in/yourname")
    github = st.text_input("GitHub / Portfolio", placeholder="https://github.com/yourname")
    skills = st.text_area("Skills (comma-separated)", placeholder="Python, C++, SQL, Machine Learning")
    experience = st.text_area("Work Experience", placeholder="Describe briefly")
    job_description = st.text_area("Paste the Job Description", placeholder="Paste job details here")

    submit_button = st.form_submit_button(label="Generate")

if submit_button:
    if not all([name, email, phone, skills, experience, job_description]):
        st.warning("⚠️ Please fill out all required fields!")
    else:
        with st.spinner("🛠 Generating Resume & Cover Letter..."):
            job_keywords = extract_job_keywords(job_description)
            resume = format_resume(f"Name: {name}\nEmail: {email}\nPhone: {phone}\nLinkedIn: {linkedin}\nGitHub: {github}\nSkills: {skills}\nExperience: {experience}", job_keywords)
            cover_letter = format_cover_letter(f"Name: {name}\nEmail: {email}\nPhone: {phone}\nLinkedIn: {linkedin}\nGitHub: {github}\nSkills: {skills}\nExperience: {experience}", job_description)

            resume_filename = f"{name.replace(' ', '_')}_Resume.pdf"
            cover_letter_filename = f"{name.replace(' ', '_')}_Cover_Letter.pdf"

            save_as_pdf(resume, resume_filename)
            save_as_pdf(cover_letter, cover_letter_filename)

        st.success("✅ Resume & Cover Letter Generated Successfully!")

        # Display Generated Content
        st.subheader("📄 Generated Resume")
        st.text_area("Resume Preview", resume, height=250)

        st.subheader("✉️ Generated Cover Letter")
        st.text_area("Cover Letter Preview", cover_letter, height=250)

        # Download Buttons
        with open(resume_filename, "rb") as file:
            st.download_button("⬇️ Download Resume", file, file_name=resume_filename, mime="application/pdf")

        with open(cover_letter_filename, "rb") as file:
            st.download_button("⬇️ Download Cover Letter", file, file_name=cover_letter_filename, mime="application/pdf")
