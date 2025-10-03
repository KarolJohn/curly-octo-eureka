from transformers import pipeline

# This line creates our AI "pipeline".
# The first time it runs, it will download the pre-trained model from the internet.
sentiment_pipeline = pipeline("sentiment-analysis")

def get_sentiment(text: str):
    """Takes a string of text and returns the sentiment analysis result."""
    result = sentiment_pipeline(text)
    # The pipeline returns a list containing a dictionary, e.g., [{'label': 'POSITIVE', 'score': 0.99}]
    # We just want the dictionary itself.
    return result[0]