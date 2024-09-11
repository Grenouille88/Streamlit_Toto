import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.title("My Dsh")

#df=pd.read_csv("CMF.csv")

#if st.checkbox("Afficher le jeu de données"):
#  st.write(df)

#matricule=df.EMPLOYEE_ID.unique()
#mat=st.selectbox("Selectionnez votre matricule",matricule)

#st.slider("Selectionnez une raison",min_value=20, max_value=100,value=30,step=1)

#st.write(df[df.EMPLOYEE_ID==mat])


#import streamlit as st
#import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    #st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    #st.write(dataframe)
  
    var=st.selectbox("Selectionnez votre matricule",dataframe.columns)
    st.write(var)
    sns.histplot(dataframe.LABEL_TZ)
    
    sns.histplot(data=dataframe,           # Jeu de données
             x='LABEL_TZ',           # Variable sur l'axe X
             bins=12,           # Nombre de barres
             kde=True,          # Ajout de la courbe de densité
             color='Red'    # Couleur des barres
             )
