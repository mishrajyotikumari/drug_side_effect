import streamlit as st
import pandas as pd

df = pd.read_csv("data/drugs_side_effects_drugs_com.csv")

st.title("⚖️ Compare Drugs")

d1 = st.selectbox("Drug 1", df["generic_name"].unique())
d2 = st.selectbox("Drug 2", df["generic_name"].unique())

if d1 and d2:
    st.dataframe(df[df["generic_name"].isin([d1, d2])])
