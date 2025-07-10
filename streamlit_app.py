import streamlit as st
import pandas as pd

st.title("Simple Data App")

uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df)
    st.write("Summary:")
    st.write(df.describe())
