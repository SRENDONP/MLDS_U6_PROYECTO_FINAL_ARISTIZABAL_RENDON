import streamlit as st
from utils import *

# Set page configuration for theme and title
st.set_page_config(page_icon="👨‍⚕️", page_title="Pneumonia Detection", layout="centered")

st.header("Project :ambulance:", anchor="large")

# Title and image upload
st.image("https://img.freepik.com/vector-gratis/concepto-neumonia-coronavirus_23-2148518517.jpg?w=996&t=st=1703690947~exp=1703691547~hmac=6360ca8036854f4354c70ba292a11421de7f22a633398ea7c25d821c5dd0ffb9", width=750)
st.title("Pneumonia Detection by Virus or Bacteria :mask:")

st.markdown("### Project Summary")
st.markdown("""
    **Project Objective:** Develop an AI system to diagnose pneumonia and determine its origin (viral or bacterial) from chest X-rays.
    
    **Project Team:**
    - Sebastián Rendón Patiño
    - Andrés Felipe Aristizábal Miranda
""")

c30, c31 = st.columns([9, 1])  
    
with c30:
    st.markdown("""
    ## Upload your X-ray image in .jpeg format
""")
    uploaded_file = st.file_uploader("", type="jpeg", key="1")
    if uploaded_file is not None:
        with st.spinner('Analyzing image...'):
            # Logic to read data and predict
            data = read_data(uploaded_file)
            model = load_model() 
            prediction = predict(model=model, data=data)
            category = get_category(prediction=prediction)
            
            # Display results
            if category == 'Normal':
                st.success("The X-ray image corresponds to a healthy person.")
            elif category == 'Bacteria':
                st.success("The X-ray image corresponds to a person with bacterial pneumonia.")
            elif category == 'Virus':
                st.success("The X-ray image corresponds to a person with viral pneumonia.")

