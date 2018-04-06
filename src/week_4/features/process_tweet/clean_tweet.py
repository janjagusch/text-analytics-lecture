from week_4.features.process_text.clean import clean_text

def clean_tweet(tweet):
    """Cleans text of tweet."""
    tweet.cleaning_log, tweet.text_cleaned = clean_text(tweet.text_raw, tokenize=True)