from utils.utils import data_from_pickle


def load_tweets():
    """Load cleaned tweets into session."""
    return data_from_pickle('02_cleaned/trump_tweets.pkl')