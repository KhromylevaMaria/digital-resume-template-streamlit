import streamlit as st

# --- GENERAL SETTINGS ---
NAME = "Pavel Chocholous"

st.set_page_config(page_title="Nadpis stránky", page_icon=":sunglasses:")

# -- TADY SE UDELA SIDE MENU
with st.sidebar:
    my_radio = st.radio("Wow effect radio button", {
        "Item 1": "Item 1 long description",
        "Item 2": "Item 2 long description"
    })

# --- TADY DVA SLOUPECKY NAHORE NA STRANCE
col1, col2 = st.columns(2, gap="small")

with col1:
    st.title("Nějaký text")
    st.write("Nějaký další text")

with col2:
    st.title(NAME)
    st.write("Hehe")


# --- A TADY SE MENI, CO JE POD NIMA, PODLE VYBRANEHO BUTTONKU V SIDE MENU
if my_radio == "Item 1":
    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Experience & Qulifications")
    st.write("""
    - ✔️ 7 Years expereince extracting actionable insights from data
    - ✔️ Strong hands on experience and knowledge in Python and Excel
    - ✔️ Good understanding of statistical principles and their respective applications
    - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    """)

if my_radio == "Item 2":
    # --- SKILLS ---
    st.write('\n')
    st.subheader("Hard Skills")
    st.write("""
    - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
    - 📊 Data Visulization: PowerBi, MS Excel, Plotly
    - 📚 Modeling: Logistic regression, linear regression, decition trees
    - 🗄️ Databases: Postgres, MongoDB, MySQL
    """)