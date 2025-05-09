import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.express as px 
import pickle
import sklearn
import numpy as np
with open("model.pickle","rb") as m:
    model = pickle.load(m)

gpa1 = pd.read_csv('tallergpa1.csv')

st.title("Taller GPA")

tab1, tab2, tab3 = st.tabs(['Tab 1','Tab 2', 'Tab 3'])

with tab1:

    fig, ax = plt.subplots(1,4 ,  figsize=(10,4))

    tab_freq = gpa1['segundo_año'].value_counts().sort_index()
    ax[0].bar(tab_freq.index, tab_freq.values)

    tab_freq = gpa1['juvenil'].value_counts().sort_index()
    ax[1].bar(tab_freq.index,tab_freq.values)


    ax[2].hist(gpa1['edad'], bins =30)


    ax[3].hist(gpa1['promedio'], bins =30)






    st.pyplot(fig)


with tab2:

    fig, ax = plt.subplots(1, 3, figsize=(10,4))
    ax[0].scatter(gpa1['edad'],gpa1['promedio'])

    ax[1].scatter(gpa1['segundo_año'],gpa1['promedio'])

    ax[2].scatter(gpa1['juvenil'],gpa1['promedio'])

    






    








    st.pyplot(fig)

with tab3:

    edad = st.slider("Edad",0,90)
    promedio = st.slider("Promedio universidad",0,5)
    segundo_año = st.selectbox('Estudiante de segundo año',['Si','No'])
    if segundo_año == 'Si' :
        segundo_año = 1
    else:
        segundo_año = 0
        

        
    juvenil = st.selectbox('Estudiante joven',['Si','No'])
    if juvenil == 'Si' :
        juvenil = 1
    else:
        juvenil = 0
        
    if st.button("Predecir"):

        pred = model.predict(np.array([[edad,
                                     segundo_año,
                                     juvenil]]))
        st.write(pred[0])
