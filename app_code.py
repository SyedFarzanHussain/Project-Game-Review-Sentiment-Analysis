import streamlit as st
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import requests

# Load the games dataset
data = pd.read_csv("games.csv", usecols=["app_id", "title"])

# Function to fetch the game header image
def get_game_header_image(app_id):
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if str(app_id) in data:
            game_data = data[str(app_id)]
            if "data" in game_data:
                game_info = game_data["data"]
                if "header_image" in game_info:
                    return game_info["header_image"]
    return "NA"  # Return "NA" if header image URL not found

# Load the sentiment analysis model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Streamlit app
st.title("Game Review Sentiment Analyzer")

# Dropdown to select a game
selected_game = st.selectbox("Select a Game", data['title'])

# Find the app_id for the selected game
app_id = data[data['title'] == selected_game]['app_id'].values[0]

# Fetch and display the game header image
image_url = get_game_header_image(app_id)
if image_url != "NA":
    st.image(image_url, caption=selected_game, use_column_width=True)
else:
    st.write("Image not available")

# Input for the review
review = st.text_area("Write your review here:")

# Sentiment analysis
if st.button("Analyze Sentiment"):
    if review:
        tokens = tokenizer.encode(review[:512], return_tensors='pt')
        result = model(tokens)
        sentiment = int(torch.argmax(result.logits)) + 1
        st.write(sentiment)
        
        # Display the sentiment result
        #if sentiment == 1 or sentiment == 2:
            #st.write("Sentiment: Negative")
        #elif sentiment == 3:
            #st.write("Sentiment: Neutral")
        #else:
            #st.write("Sentiment: Positive")
    else:
        st.write("Please write a review to analyze.")
