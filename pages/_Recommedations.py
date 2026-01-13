import streamlit as st
import pandas as pd

df = pd.read_csv("data/drugs_side_effects_drugs_com.csv")

st.title("🧠 Drug Insights")

st.metric("Total Drugs", df["generic_name"].nunique())
st.metric("Diseases Covered", df["medical_condition"].nunique())
st.metric("Avg Rating", round(df["rating"].mean(), 2))
