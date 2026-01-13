import streamlit as st
import pandas as pd

df = pd.read_csv("data/drugs_side_effects_drugs_com.csv")

st.title("⭐ Top Rated Drugs")

top = df.sort_values("rating", ascending=False).head(10)
st.dataframe(top[["generic_name", "rating"]])
