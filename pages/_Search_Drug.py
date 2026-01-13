import streamlit as st
import pandas as pd

st.title("🔍 Search Drug")

df = pd.read_csv("data/drugs_side_effects_drugs_com.csv")

drug = st.text_input("Enter drug name")

if drug:
    result = df[df["generic_name"].str.contains(drug, case=False, na=False)]
    if result.empty:
        st.warning("No result found")
    else:
        st.dataframe(result.head(20))
