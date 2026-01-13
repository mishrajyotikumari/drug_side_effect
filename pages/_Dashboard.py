import streamlit as st
import pandas as pd

df = pd.read_csv("data/drugs_side_effects_drugs_com.csv")

st.title("📊 Dashboard")

st.bar_chart(df["pregnancy_category"].value_counts())
st.line_chart(df["rating"])
