import streamlit as st
import pandas as pd

df = pd.read_csv("data/drugs_side_effects_drugs_com.csv")

st.title("⚠️ Drug Side Effects")

drug = st.selectbox("Select Drug", df["generic_name"].dropna().unique())

if drug:
    row = df[df["generic_name"] == drug].iloc[0]
    st.warning(row.get("side_effects", "No data available"))
