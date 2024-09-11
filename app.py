import streamlit as st
import pandas as pd

st.title("My Dsh")

df=pd.read_csv("CMF.csv")

if st.checkbox("Afficher le jeu de données"):
  st.write(df)

matricule=df.EMPLOYEE_ID.unique()
mat=st.selectbox("Selectionnez votre matricule",matricule)


st.write(df[df.EMPLOYEE_ID==mat])
