import streamlit as st
import pandas as pd

st.set_page_config(page_title="Budget App", page_icon=":moneybag:", layout="wide")

if __name__ == '__main__':
  file_path="monefy-2023-12-22_03-09-21.csv"
  # data = pd.read_csv(file_path, delimiter=",")
  data = pd.DataFrame(file_path)
  st.write(data)
  # data=st.dataframe(data)
  st.bar_chart(data)
