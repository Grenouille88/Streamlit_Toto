import streamlit as st
import pandas as pd

st.title("My Dsh")

df=pd.read_csv("CMF.csv")

if st.checkbox("Afficher le jeu de données"):
  st.write(df)

matricule=df.EMPLOYEE_ID.unique()
mat=st.selectbox("Selectionnez votre matricule",matricule)

st.slider("Selectionnez une raison",min_value=20, max_value=100,value=30,step=1)

st.write(df[df.EMPLOYEE_ID==mat])
