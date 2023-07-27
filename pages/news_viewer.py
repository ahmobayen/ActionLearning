import streamlit as st
import finnhub

import datetime
from pages.utils.Sentiment_analysis import get_sentiment_scores, get_sentiment_label

# Replace YOUR_API_KEY with your actual Finnhub API key
finnhub_client = finnhub.Client(api_key="cj16eq1r01qhv0uhjss0cj16eq1r01qhv0uhjssg")


def convert_unix_to_datetime(unix_time):
    return datetime.datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')


def get_company_news(stock_code, start_date, end_date):
    raw_news = finnhub_client.company_news(stock_code, _from=start_date, to=end_date)
    if raw_news and "error" not in raw_news:
        # Filter out the 'image' and 'id' fields and convert timestamps
        filtered_news = [{key: value for key, value in item.items() if key not in ['image', 'id']} for item in raw_news]
        for item in filtered_news:
            item['datetime'] = convert_unix_to_datetime(item['datetime'])
            sentiment_scores = get_sentiment_scores(item['headline'])
            item['Negative'] = sentiment_scores[0]
            item['Neutral'] = sentiment_scores[1]
            item['Positive'] = sentiment_scores[2]
        return filtered_news
    return None


def main():
    st.title("FinS - Financial news with Sentiment Analysis ")

    # Get user input for stock code and date range
    stock_code = st.text_input("Enter a stock code (e.g., AAPL, GOOGL)", "AAPL")

    start_date = st.date_input("Select the start date")
    end_date = st.date_input("Select the end date")

    # Fetch and display the news
    if st.button("Get News"):
        if start_date > end_date:
            st.error("Error: Start date cannot be after end date.")
        else:
            news = get_company_news(stock_code, str(start_date), str(end_date))
            if news:
                # Create a DataFrame with the modified data
                import pandas as pd
                df = pd.DataFrame(news)
                df['datetime'] = pd.to_datetime(df['datetime'])
                sentiment_labels = df.apply(
                    lambda row: get_sentiment_label([row['Negative'], row['Neutral'], row['Positive']]), axis=1)
                df['Sentiment'] = sentiment_labels
                df['Negative'] = df['Negative'].apply(lambda score: f"{score:.2%}")
                df['Neutral'] = df['Neutral'].apply(lambda score: f"{score:.2%}")
                df['Positive'] = df['Positive'].apply(lambda score: f"{score:.2%}")

                # Display the news table with clickable links
                st.dataframe(df[['datetime', 'headline', 'Sentiment', 'Negative', 'Neutral', 'Positive', 'related',
                                 'source', 'summary', 'url']], height=600)
            else:
                st.error("No news found for the given stock and date range.")


if __name__ == "__main__":
    main()
