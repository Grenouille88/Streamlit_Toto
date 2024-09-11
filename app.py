import streamlit as st
import pandas as pd

st.title("My Dsh")

df=pd.read_csv("CMF.csv")

st.write(df)
