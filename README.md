# Game Review Sentiment Analyzer

This project is a web application that allows users to analyze the sentiment of their reviews on different games. The app is built using Streamlit and leverages a pre-trained Transformer model (DistilBERT) from Hugging Face to classify the sentiment of the reviews. The app is designed to handle reviews of up to 512 words.

## Features

- **Game Selection**: Users can select a game from a dropdown list populated with titles from a provided dataset.
- **Sentiment Analysis**: The app analyzes the sentiment of a user-provided review, classifying it as positive or negative.

## How It Works

1. **Data Loading**: The app loads a dataset containing game titles and their corresponding Steam `app_id`s.

2. **Game Selection**: Users select a game from the dropdown. The app uses the selected game's `app_id` to fetch and display the game's header image from the Steam Store.

3. **Review Input**: Users can input their review of the game into a text area.

4. **Sentiment Analysis**: The review is tokenized and passed through the DistilBERT model to predict the sentiment. The model outputs it as a positive or negative review
