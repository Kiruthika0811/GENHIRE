import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="AutoHire Dashboard", layout="wide")

st.title("🤖 AutoHire: Smart Recruitment Dashboard")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📄 Job Descriptions", "👤 Candidates", "🧮 Matches", "📅 Interviews"])

with tab1:
    st.subheader("Uploaded Job Descriptions")
    jd_df = pd.read_excel("../data/job_descriptions.xlsx")
    st.dataframe(jd_df)

with tab2:
    st.subheader("Candidate Profiles")
    cv_df = pd.read_csv("../data/cvs.csv")
    st.dataframe(cv_df)

with tab3:
    st.subheader("Match Scores (To be generated)")
    st.info("Once agents are ready, this tab will show CV ↔ JD matches.")

with tab4:
    st.subheader("Scheduled Interviews (To be generated)")
    st.warning("Interview scheduling module not implemented yet.")
