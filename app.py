import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)


df = pd.read_csv('rev_cleaned.csv')

st.set_page_config(
    page_title="Product Review Analysis",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
#EDA

def eda():
    avg_rating = df['Score'].mean()     #finds the average rating
    st.metric(label= 'Average Rating',value= avg_rating)

    # for positive sentiment
    positive_reviews = df[df["sc"] == 'Positive']['Text'].sample(n=1000, random_state=42).str.cat(sep=' ')
    st.subheader('Word Cloud For postive reviews')
    plt.figure(figsize=(20, 20))
    wc = WordCloud(width=1600, height=800).generate(positive_reviews)
    plt.imshow(wc)
    st.pyplot()

    negative_reviews = df[df["sc"] == 'Negative']['Text'].sample(n=1000, random_state=42).str.cat(sep=' ')
    st.subheader('Word Cloud For negative reviews')

    plt.figure(figsize=(20, 20))
    wc = WordCloud(width=1600, height=800).generate(negative_reviews)
    plt.imshow(wc)
    st.pyplot()

#Sentiment Analysis





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
        eda()
    else:
        st.title('Sentiment Analysis')
        sentiment_analysis()

else:
    st.title('Input Review')

