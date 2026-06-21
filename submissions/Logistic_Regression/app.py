import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title='Diabetes Predictor', page_icon='🏥', layout='centered')

st.title('🏥 Diabetes Prediction App')
st.markdown('### Logistic Regression Model - Pima Indians Diabetes Dataset')
st.markdown('---')

@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as f:
        return pickle.load(f)

model_data = load_model()
model = model_data['model']
scaler = model_data['scaler']

st.sidebar.header('Enter Patient Information')

pregnancies = st.sidebar.slider('Pregnancies', 0, 17, 1)
glucose = st.sidebar.slider('Glucose (mg/dL)', 0, 200, 120)
blood_pressure = st.sidebar.slider('Blood Pressure (mm Hg)', 0, 122, 70)
skin_thickness = st.sidebar.slider('Skin Thickness (mm)', 0, 100, 20)
insulin = st.sidebar.slider('Insulin (mu U/ml)', 0, 846, 80)
bmi = st.sidebar.slider('BMI', 0.0, 70.0, 32.0, 0.1)
dpf = st.sidebar.slider('Diabetes Pedigree Function', 0.0, 2.5, 0.47, 0.01)
age = st.sidebar.slider('Age', 21, 81, 33)

input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, 
                        insulin, bmi, dpf, age]])

input_scaled = scaler.transform(input_data)
prediction = model.predict(input_scaled)[0]
probability = model.predict_proba(input_scaled)[0][1]

st.markdown('## Prediction Result')

col1, col2 = st.columns(2)

with col1:
    if prediction == 1:
        st.error(f'🔴 **Diabetic**')
    else:
        st.success(f'🟢 **Non-Diabetic**')

with col2:
    st.metric('Diabetes Probability', f'{probability:.1%}')

st.progress(float(probability))

st.markdown('---')
st.markdown('### Input Summary')
col1, col2, col3 = st.columns(3)
with col1:
    st.metric('Pregnancies', pregnancies)
    st.metric('Glucose', f'{glucose} mg/dL')
    st.metric('Blood Pressure', f'{blood_pressure} mm Hg')
with col2:
    st.metric('Skin Thickness', f'{skin_thickness} mm')
    st.metric('Insulin', f'{insulin} mu U/ml')
    st.metric('BMI', f'{bmi:.1f}')
with col3:
    st.metric('DPF', f'{dpf:.3f}')
    st.metric('Age', age)

st.markdown('---')
st.markdown('*Model: Logistic Regression trained on Pima Indians Diabetes Database*')

print('app.py created successfully!')
