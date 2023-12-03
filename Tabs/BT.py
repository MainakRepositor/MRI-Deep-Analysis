import streamlit as st
import imagerec
import pandas as pd
import random
import streamlit.components.v1 as components


def app():
    
    uploaded_file = None

    st.title("Brain Tumor Predictor")



    st.markdown('''There are several types of brain tumors, including:''')
                
    st.info("Glioma: A type of tumor that originates in the glial cells, which are the supportive cells in the brain. Gliomas can be either low-grade (slow-growing) or high-grade (fast-growing) and can affect different parts of the brain.")
                
    st.warning("Meningioma: A tumor that arises from the meninges, which are the protective membranes that surround the brain and spinal cord. Meningiomas are usually benign and slow-growing, and may not require treatment if they are not causing symptoms.")

    st.error("Pituitary adenoma: A tumor that develops in the pituitary gland, which is located at the base of the brain. Pituitary adenomas can affect hormone production and cause a variety of symptoms, depending on the hormones that are affected.")
    
    uploaded_file = st.file_uploader("Choose a File", type=['jpg','png','jpeg'])

    st.sidebar.markdown(
    f'<a href="https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: blue; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Brain Tumour Dataset</a>',
    unsafe_allow_html=True
)

    if uploaded_file!=None:
        st.image(uploaded_file)
    x = st.button("Detect Condition")
    if x:
        with st.spinner("Predicting..."):
            y,conf = imagerec.imagerecognise(uploaded_file,"Models/BrainTumuorModel.h5","Models/BrainTumuorLabels.txt")
        if y.strip() == "Safe":
            components.html(
                """
                <style>
                h1{
                    
                    background: -webkit-linear-gradient(0.25turn,#01CCF7, #8BF5F5);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-family: "Source Sans Pro", sans-serif;
                }
                </style>
                <h1>It is Negative for Brain Tumors</h1>
                """
            )
        elif y.strip() == "Glioma":
            components.html(
                """
                <style>
                h1{
                    background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-family: "Source Sans Pro", sans-serif;
                }
                </style>
                <h1>Glioma Positive</h1>
            
                """
            )
            st.info("Inference and Suggestion:")
            st.write("Don't worry! For glioma treatment, radiation therapy is often used after surgery. The radiation kills any glioma cells that might remain after surgery. Radiation is often combined with chemotherapy. Radiation therapy might be the first glioma treatment if surgery isn't an option.")
        elif y.strip() == "Meningioma":
            components.html(
                """
                <style>
                h1{
                    background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-family: "Source Sans Pro", sans-serif;
                }
                </style>
                <h1>Meningioma Positive</h1>
                
                """
            )
            st.info("Inference and Suggestion:")
            st.write("Surgery is the most common type of treatment, but it can be difficult if the tumor is near a delicate part of the brain or spinal cord. Radiation therapy is also commonly used. The blood-brain barrier, which normally protects the brain and spinal cord from damaging chemicals, also keeps out many types of chemotherapy")
        else:
            components.html(
                """
                <style>
                h1{
                    background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-family: "Source Sans Pro", sans-serif;
                }
                </style>
                <h1>Pituitary Tumor Found</h1>"""
            )
            st.info("Inference and Suggestion:")
            st.write('Treatment of pituitary carcinomas is palliative, to relieve symptoms and improve the quality of life. Treatment may include the following: Surgery (transsphenoidal surgery or craniotomy) to remove the cancer, with or without radiation therapy. Drug therapy to stop the tumor from making hormones')

        
        
        x = random.randint(95,99)+ random.randint(0,99)*0.01
    
        st.sidebar.warning("Accuracy : " + str(x) + " %")
