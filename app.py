import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Product Review Analysis",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


st.sidebar.title('Product Review Analysis')
option = st.sidebar.selectbox('Select one', ['Analysis', 'Input Review'])
if option == "Analysis":
    with st.sidebar:
        add_radio = st.radio(
            "Choose analysis",
            ("EDA", "Sentiment Analysis")
        )
    if add_radio == 'EDA':
        st.title('EDA')
    else:
        st.title('Sentiment Analysis')

else:
    st.title('Input Review')

