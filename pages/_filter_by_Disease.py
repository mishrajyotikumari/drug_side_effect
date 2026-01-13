import streamlit as st
import pandas as pd

df = pd.read_csv("data/drugs_side_effects_drugs_com.csv")

st.title("🦠 Filter Drugs by Disease")

disease = st.text_input("Enter disease (example: Acne, Cancer)")

if disease:
    result = df[df["medical_condition"].str.contains(disease, case=False, na=False)]
    st.dataframe(result[["generic_name", "medical_condition"]].head(20))
