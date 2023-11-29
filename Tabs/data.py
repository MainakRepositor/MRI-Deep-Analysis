"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st


def app(df):
    """This function create the Data Info page"""

    # Add title to the page
    st.title("Data Info page")

    # Add subheader for the section
    st.subheader("View Data")

    # Create an expansion option to check the data
    with st.expander("View data"):
        st.dataframe(df)

    # Create a section to columns values
    # Give subheader
    st.subheader("Columns Description:")

    # Create a checkbox to get the summary.
    if st.checkbox("View Summary"):
        st.dataframe(df.describe())

    # Create multiple check box in row
    col_name, col_dtype, col_data = st.columns(3)

    # Show name of all dataframe
    with col_name:
        if st.checkbox("Column Names"):
            st.dataframe(df.columns)

    # Show datatype of all columns 
    with col_dtype:
        if st.checkbox("Columns data types"):
            dtypes = df.dtypes.apply(lambda x: x.name)
            st.dataframe(dtypes)
    
    # Show data for each columns
    with col_data: 
        if st.checkbox("Columns Data"):
            col = st.selectbox("Column Name", list(df.columns))
            st.dataframe(df[col])


    with st.expander("Research Info and Calculations"):
        st.info("Calculations and Inference from EEG-MRI")
        st.markdown('''https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7485780/''')

        st.info("EEG Electrode Schematics for deeper insights of MRI-Scan")
        st.image('https://imgs.search.brave.com/AcUMd9jj7kZ3G04k1mePqExMq-792Nx_ODr1ea-6oRY/rs:fit:500:0:0/g:ce/aHR0cHM6Ly93d3cu/ZWJtZS5jby51ay9p/bWFnZXMvYXJ0cy9l/ZWcvMTAtMjAtZWxl/Y3Ryb2RlLXBsYWNl/bWVudC5qcGc')

 