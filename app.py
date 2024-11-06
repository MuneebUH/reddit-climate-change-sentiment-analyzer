import streamlit as st
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import matplotlib.pyplot as plt
import seaborn as sns

# Download the VADER lexicon
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Streamlit App Title
st.title("Reddit Climate Change Sentiment Analyzer")
st.write("Analyze sentiment of Reddit comments on climate change using VADER Sentiment Analysis.")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# Check if a file is uploaded
if uploaded_file is not None:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Ensure 'comment' column exists for analysis
    if 'comment' not in df.columns:
        st.error("CSV file must contain a 'comment' column for sentiment analysis.")
    else:
        # Display a sample of the uploaded data
        st.subheader("Uploaded Data Sample")
        st.write(df.head())
        
        # Run VADER sentiment analysis on the comments
        st.subheader("Running Sentiment Analysis...")
        df['sentiment_score'] = df['comment'].apply(lambda x: sia.polarity_scores(str(x))['compound'])
        
        # Categorize the sentiment scores
        def categorize_sentiment(score):
            if score >= 0.05:
                return 'Positive'
            elif score <= -0.05:
                return 'Negative'
            else:
                return 'Neutral'
        
        df['sentiment_category'] = df['sentiment_score'].apply(categorize_sentiment)
        
        # Show sentiment analysis results
        st.write("Sentiment Analysis Completed!")
        st.write(df[['comment', 'sentiment_score', 'sentiment_category']].head())

        # Visualize sentiment distribution
        st.subheader("Sentiment Distribution")
        sentiment_counts = df['sentiment_category'].value_counts()

        # Plot sentiment distribution
        fig, ax = plt.subplots()
        sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="viridis", ax=ax)
        ax.set_title("Distribution of Sentiment Categories")
        ax.set_xlabel("Sentiment Category")
        ax.set_ylabel("Count")
        st.pyplot(fig)

        # Display Data with Sentiment Scores
        st.subheader("Full Dataset with Sentiment Scores")
        st.write(df)
        
        # Option to download analyzed data
        st.subheader("Download Analyzed Data")
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name='analyzed_sentiment_data.csv',
            mime='text/csv'
        )
