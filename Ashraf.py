import streamlit as st
import joblib
import pandas as pd
import sklearn
model=joblib.load('Model.h5')
inputs=joblib.load('input.h5')
def predict(gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status,Glucose_level):
    test_df=pd.DataFrame(columns=inputs)
    test_df.at[0,'gender']=gender
    test_df.at[0,'age']=age
    test_df.at[0,'hypertension']=hypertension
    test_df.at[0,'heart_disease']=heart_disease
    test_df.at[0,'ever_married']=ever_married
    test_df.at[0,'work_type']=work_type
    test_df.at[0,'Residence_type']=Residence_type
    test_df.at[0,'avg_glucose_level']=avg_glucose_level
    test_df.at[0,'bmi']=bmi
    test_df.at[0,'smoking_status']=smoking_status
    test_df.at[0,'Glucose_level']=Glucose_level
    result=model.predict(test_df)[0]
    return result
def main():
    st.title('Strock predction')
    gender=st.selectbox('gender',['Male', 'Female'])
    age=st.slider('age',min_value= 1.0,max_value= 82.0,value=10.0,step=1.0)
    hypertension=st.selectbox('hypertension',[0,1])
    heart_disease=st.selectbox('heart_disease',[0,1])
    ever_married=st.selectbox('ever_married',['Yes', 'No'])
    work_type=st.selectbox('work_type',['Private','Self-employed ','Govt_job','children','Never_worked'])
    Residence_type=st.selectbox('Residence_type',['Urban', 'Rural'])
    avg_glucose_level=st.slider('avg_glucose_level',min_value= 55.0,max_value= 271.0,value=55.0,step=0.1)
    bmi=st.slider('bmi',min_value=10.3,max_value=49.9,value=10.3,step=0.1)
    smoking_status=st.selectbox('smoking_status',['never smoked', 'Unknown','formerly smoked','smokes'])
    Glucose_level=st.selectbox('Glucose_level',['low','normal', 'diabetes','prediabetes'])
    if st.button('predict'):
        result=predict(gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status,Glucose_level)
        st.write('predict is',result)
if __name__ =='__main__':
    main()
