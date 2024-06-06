from pathlib import Path
import time
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_MariaKhromyleva.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Maria Khromyleva"
PAGE_ICON = ":wave:"
NAME = "Maria Khromyleva"
DESCRIPTION = """
Data Analyst with over 15 years of IT experience, proficient in project management, and skilled in Python, SQL, and Tableau.
"""
EMAIL = "khromyleva.maria@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/mariakhromyleva",
    "GitHub": "https://github.com/mariakhromyleva",
    "Twitter": "https://twitter.com/mariakhromyleva"
}
PROJECTS = {
    "🏆 Reporting System with Dashboards - Reduced report preparation from 1 day to 5 minutes":
    "https://github.com/mariakhromyleva/reporting_system",
    "🏆 Automated Accounting Reporting System for a 15-company holding - Shortened reporting time from 10 days to 2 days":
    "https://github.com/mariakhromyleva/accounting_system",
}
SECTIONS = {
    "Experience": "Exp",
    "Tech stack": "Hard-skills",
    "Education": "Education",
    "Portfolio": "Projects",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- LOAD PDF ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- PROFILE PIC ---
profile_pic = Image.open(profile_pic)

with st.sidebar:
    my_radio = st.radio("Select Section", list(SECTIONS.keys()))
    awesomeness_level = st.slider("Rate my profile", 0, 10, 10)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download CV",
        data=PDFbyte,
        file_name="MariaKhromyleva_CV.pdf",
        mime="application/pdf"
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

if my_radio == "Experience":
    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Experience & Qualifications")
    st.write("""
    - ✔️ Project development and implementation of IT systems and KPIs
    - ✔️ Led IT teams and infrastructure maintenance for 300 users
    - ✔️ Expertise in data analysis and business process automation
    """)

if my_radio == "Tech stack":
    # --- SKILLS ---
    st.write('\n')
    st.subheader("Hard Skills")
    st.write("""
    - 👩‍💻 Programming: Python, SQL
    - 📊 Data Visualization: Tableau
    - 🗄️ Project Management: Jira, Microsoft Project, Confluence
    """)

if my_radio == "Education":
    # --- EDUCATION ---
    st.write('\n')
    st.subheader("Education")
    st.write("""
    - 🎓 Northern (Arctic) Federal University, Degree in Forest Engineering
    - 🎓 Continuous learning through online courses in Python, SQL, Tableau
    """)

if my_radio == "Portfolio":
    # --- PROJECTS & ACCOMPLISHMENTS ---
    st.write('\n')
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")

for i in range(awesomeness_level + 1):
    with st.sidebar:
        st.write("🎉" * i)
    time.sleep(0.2)
