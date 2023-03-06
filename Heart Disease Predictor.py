import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

heart_disease = pickle.load(open('C:/Users/kashy/OneDrive/Desktop/Heart_disease/sample model/heart_disease_model.sav','rb'))

with st.sidebar:
    selected = option_menu('Prediction',['Heart Disease Prediction'],icons = ['activity'],default_index=0)

if(selected=='Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    
    col1,col2,col3,col4 = st.columns(4)

    with col1:
        age  = st.text_input("Your Age")
    
    with col2:
          sex = st.text_input("Your sex")
    with col3:
         cp =  st.text_input("chest pain type")
    with col4:
         trestbps =  st.text_input("chest pain pressure")
    with col1:
       chol =  st.text_input("serum cholestoral in mg/dl")
    with col2:
        fbs = st.text_input("fasting blood sugar")
    with col3:
         restecg =  st.text_input("electrocardiographic")

    with col4:
       thalach= st.text_input("maximum heart rate ")

    with col1:
       exang = st.text_input("exercise induced angina")
    with col2:
       oldpeak = st.text_input("oldpeak")
    with col3:
        slope = st.text_input("slope of the peak exercise ")

    with col4:
        ca = st.text_input("number of major vessels")
    
    with col1:
        thal = st.text_input("thal")
        
    heart_disease_diag = ''

    if st.button('Test Result'):
       heart_disease_pred = np.array([[age, sex, cp, trestbps, chol, fbs,restecg, thalach,exang, oldpeak, slope, ca, thal]])
       if(heart_disease_pred[0]==1):
        heart_disease_diag = 'You have Heart Disease'
       else:
        heart_disease_diag = "You don't have Heart Disease"
    
    st.success(heart_disease_diag) 

