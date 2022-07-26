# Import libraries
import joblib
import streamlit as st

# Define functions
with open('diabetes_model.pkl', 'rb') as model:
    classifier = joblib.load(model)
    
def predictor(Pregnancies, Glucose, BloodPressure, Age):
    global classifier
    prediction = classifier.predict([[Pregnancies, Glucose, BloodPressure,  Age]])
    if prediction == 0:
        return 'The patient is not diabetic'
    else: 
        return 'The patient is diabetic'
   
# Create an app
def main():
    st.title('Diabetes Prediction App')
    
    preg = st.number_input('Pregnancies')
    glucose = st.number_input('Glucose')
    bp = st.number_input('BloodPressure')
    age = st.number_input('Age')
    
    # Predict
    if st.button('Predict'):
        diabetes_prediction = predictor(preg, glucose, bp, age)
        st.success(f' {diabetes_prediction}')
        
if __name__ == '__main__':
    main()