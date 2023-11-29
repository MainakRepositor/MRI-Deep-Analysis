"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Prediction of eye quality.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    col1, col2 = st.columns(2)

    with col1:
        A = st.slider("AF3", int(df["AF3"].min()), int(df["AF3"].max()))
        B = st.slider("F7", int(df["F7"].min()), int(df["F7"].max()))
        C = st.slider("F3", int(df["F3"].min()), int(df["F3"].max()))
        D = st.slider("FC5", float(df["FC5"].min()), float(df["FC5"].max()))
        E = st.slider("T7", float(df["T7"].min()), float(df["T7"].max()))
        F = st.slider("P7", float(df["P7"].min()), float(df["P7"].max()))
        G = st.slider("O1", float(df["O1"].min()), float(df["O1"].max()))

    with col2:
        H = st.slider("O2", float(df["O2"].min()), float(df["O2"].max()))
        I = st.slider("P8", float(df["P8"].min()), float(df["P8"].max()))
        J = st.slider("T8", float(df["T8"].min()), float(df["T8"].max()))
        K = st.slider("FC6", float(df["FC6"].min()), float(df["FC6"].max()))
        L = st.slider("F4", float(df["F4"].min()), float(df["F4"].max()))
        M = st.slider("F8", float(df["F8"].min()), float(df["F8"].max()))
        N = st.slider("AF4", float(df["AF4"].min()), float(df["AF4"].max()))
     
    st.sidebar.info("P7 and O1 electrode positive signals signify the patient has good neural flow of electrons between the hypothalamus and the cortex, in regions of constriction and hence there is a high chance of being free from tumour or other brain anomalies. However, its suggested to consult a physician.")

    # Create a list to store all the features
    features = [A,B,C,D,E,F,G,H,I,J,K,L,M,N]

    
    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.info("MRI Analysis successful...")

        if (A > 10000 and B > 5000):
            st.warning("High risk of Pituitary tumour, but in initial stage of tumour formation")

        elif (A > 20000 and A < 90000):
            st.warning("High risk of Pituitary tumour, in the medium stage")

        elif (A > 100000):
            st.warning("High risk of Pituitary tumour, in the final stage")
            
        elif (D > 3200 and D < 7000 and B >5000):
            st.warning("High risk of Meningoma tumour, but in initial stage of tumour formation")

        elif (D > 7200 and D < 15000 and B >5000):
            st.warning("High risk of Meningoma tumour, but in medium stage of tumour formation")

        elif (D > 15200 and B >5000):
            st.warning("High risk of Meningoma tumour, but in final stage of tumour formation")

        elif (M < 2500 and N < 3500):
            st.warning("High risk of Glioma tumour, but in initial stage of tumour formation")

        elif (M < 7500 and N < 15000):
            st.warning("High risk of Glioma tumour, but in initial stage of tumour formation")

        elif (M > 25700 and N > 35800):
            st.warning("High risk of Glioma tumour, but in final stage of tumour formation")

             


        # Print the output according to the prediction
        elif (prediction == 0):
            st.success("Patient has no considerable symptoms of brain anomaly😎")
        else:
            st.error("Brain Tumour is confirmed!")
            
        
