import streamlit as st
import pandas as pd

st.set_page_config(page_title="Budget App", page_icon=":moneybag:", layout="wide")

if __name__ == '__main__':
  file_path="monefy-2023-12-22_03-09-21.csv"
  data = pd.read_csv(file_path, delimiter=",")
  column_headers = list(data.columns.values)
  st.write(column_headers)
  # Keep only expenses
  data = data[~data["category"].isin(["Salary", "Deposits"])]
  exit()
  # Convert negative expenses into positive values
  data = data["amount"].abs()
  st.bar_chart(data=data, x="category", y="amount") #, color=None, width=0, height=0, use_container_width=True)
