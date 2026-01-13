import streamlit as st
import pandas as pd

df = pd.read_csv("data/drugs_side_effects_drugs_com.csv")

st.title("🤰 Pregnancy Safety Checker")

drug = st.selectbox("Select Drug", df["generic_name"].dropna().unique())

if drug:
    category = df[df["generic_name"] == drug]["pregnancy_category"].values[0]
    st.info(f"Pregnancy Category: {category}")

    if category == "A":
        st.success("Safe in pregnancy")
    elif category in ["D", "X"]:
        st.error("Not safe in pregnancy")
    else:
        st.warning("Consult doctor")
