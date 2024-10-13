import streamlit as st
import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

sia = SentimentIntensityAnalyzer()

def classify_sentiment(compound_score):
    values = ['Positive', 'Neutral', 'Negative']
    if compound_score >= 0.5:
        return values[0]
    elif -0.5 < compound_score < 0.5:
        return values[1]
    elif compound_score <= -0.5:
        return values[2]

@st.cache_data
def overall_sentiment(i, df, choice):
    df2 = df[df[choice] == i].copy()
    counts=df2['sentiment'].value_counts().sort_values(ascending=True)
    dic = counts.to_dict()
    max_value = max(dic.values())  # maximum value
    max_keys = [k for k, v in dic.items() if v == max_value]
    return max_keys
     

st.title('Sentylser :bar_chart:')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    choice = st.selectbox('Select the column that lists the product names',df.columns)
    unique_arr = df[choice].unique()
    choice2 = st.selectbox('Select the product name you want to get the sentiment',unique_arr)
    choice3 = st.selectbox('Select the column where the review text is',df.columns)
    df2 = df[df[choice] == choice2].copy()
    df2 = df2[[choice,choice3]]
    df2['compound'] = df2[choice3].apply(lambda review: sia.polarity_scores(str(review))['compound'])
    df2['sentiment'] = df2['compound'].apply(classify_sentiment)

if st.button("Submit"):
    counts=df2['sentiment'].value_counts().sort_values(ascending=True) #sorts the counts of each sentiment
    fig, ax = plt.subplots(figsize=(11, 6))
    colours = {'Negative':'#ff4c4c','Positive':'#38d864','Neutral':'#ffff00'}
    value_colours = [colours[x] for x in counts.index] #makes sure that colours stay the same for sentiments    
    fig.patch.set_facecolor('none')
    ax.set_facecolor('none')   
    counts.plot.pie(ax=ax,autopct='%1.1f%%', colors=value_colours,textprops={'color':"black"}, labels=None)
    ax.axis('equal')
    st.pyplot(fig)

    df['compound'] = df[choice3].apply(lambda review: sia.polarity_scores(str(review))['compound'])
    df['sentiment'] = df['compound'].apply(classify_sentiment)

    df_overall = pd.DataFrame(data=unique_arr, columns=['Product'])

    counts=df['sentiment'].value_counts().sort_values(ascending=True) 
    l=[]
    for i in df_overall['Product']:
        j = overall_sentiment(i, df, choice)
        j=j[0] #if out of two values will only pick one
        k = ''.join(j)
        l.append(k)
    df_overall['sentiment'] = l

    csv = df_overall.to_csv()

    st.download_button(
        label="Download Spreadsheet file containing overall Sentiment Data for all Products",
        data=csv,
        file_name="productSentiment.csv",
        mime="text/csv",
    )    



