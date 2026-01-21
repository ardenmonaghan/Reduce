import streamlit as st
import pandas as pd

# CONSTANTS
save_path = "/Users/ardenmonaghan/Desktop/MachineLearning/Reduce/data"

st.set_page_config(page_title="ReduceDB", page_icon=":chart_with_upwards_trend:", layout="wide")
st.title("ReduceDB")
st.write("Welcome to ReduceDB, a tool for reducing data using MapReduce.")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:

    st.success("File uploaded and saved successfully")

    df = pd.read_csv(uploaded_file)

    # Showing the preview. 
    st.subheader("Preview of the uploaded file")
    st.dataframe(df.head())
    all_columns = df.columns.tolist()
    numberic_cols = df.select_dtypes(include='number').columns.tolist()

    # Write locally 
    # st.write(df)

    df.to_csv(f"{save_path}/uploaded_file.csv", index=False)

