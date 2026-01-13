import streamlit as st
import pandas as pd

df = pd.read_csv("data/drugs_side_effects_drugs_com.csv")

st.title("💊 Rx vs OTC")

rx_type = st.selectbox("Select Type", ["Rx", "OTC"])

result = df[df["rx_otc"] == rx_type]
st.dataframe(result[["generic_name", "rx_otc"]].head(20))
